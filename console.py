#!/usr/bin/python3
"""
defines the HBNB console.
"""
import cmd
import sys
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
        
clx = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review
}


class HBNBCommand(cmd.Cmd):
    """HBNB console."""

    prompt = '(hbnb) '

    def default(self, line):
        """Default behavior for cmd module when input is invalid"""
        cmds = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        pattern_match = re.search(r"\.", line)
        if pattern_match is not None:
            argl = [line[:pattern_match.span()[0]], line[pattern_match.span()[1]:]]
            pattern_match = re.search(r"\((.*?)\)", argl[1])
            if pattern_match is not None:
                command = [argl[1][:pattern_match.span()[0]], pattern_match.group()[1:-1]]
                if command[0] in cmds.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return cmds[command[0]](call)
        print("*** Unknown syntax: {}".format(line))
        return False

    def do_create(self, cls):
        """creates object classes."""
        if cls and cls in clx:
            if storage.all():
                storage.reload()
            obj = clx[cls]()
            storage.save()
            print(obj.id)
        elif cls:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_create(self):
        """docs for the command create."""
        print("creates an object of any supported class.")
        print("[usage]: create <classname>")

    def do_show(self, line):
        """defines the show command."""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        else:
            if args[0] not in clx:
                print("** class doesn't exist **")
                return
            elif len(args) == 1:
                print("** instance id missing **")            
                return
        
        cls = args[0]
        ld = args[1]
            
        key = f"{cls}.{ld}"
        storage.reload()
        
        try:
            obj = storage.all()[key]
            print(obj)
        except KeyError:
            print("** no instance found **")
        

    def help_show(self):
        """docks for the show command."""
        print("shows the string representation of an object.")
        print("[usage]: show <classname> <id>")

    def do_destroy(self, line):
        """defines the destroy command."""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        else:
            if args[0] not in clx:
                print("** class doesn't exist **")
                return
            elif len(args) == 1:
                print("** instance id missing **")            
                return
        
        cls = args[0]
        ld = args[1]
            
        key = f"{cls}.{ld}"
        storage.reload()
        
        try:
            del storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found **")
        

    def help_destroy(self):
        """docs for the destroy command."""
        print("destroys an object")
        print("[usage]: destroy <classname> <id>")

    def do_all(self, cls):
        """defines the all command."""
        if cls in clx:
            storage.reload()
            objs = storage.all()
            str_rep = []
            for key in objs:
                if cls in key:
                    str_rep.append(str(objs[key]))
            print(str_rep)
        elif cls:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_all(self):
        """docs for the all command."""
        print("shows the string representation for all objects for a class.")
        print("[usage]: all <classname>")

    def do_update(self, line):
        """defines the update command."""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        else:
            if args[0] not in clx:
                print("** class doesn't exist **")
                return
            elif len(args) == 1:
                print("** instance id missing **")            
                return
            elif len(args) == 2:
                print("** attribute name missing **")
                return
            elif len(args) == 3:
                print("** value missing **")
                return

        cls = args[0]
        ld = args[1]
        attr = args[2]
        val = args[3][1:-1]

        storage.reload()
        key = f"{cls}.{ld}"
        if key not in storage.all():
            print("** no instance found **")
            return
        
        new_attr = {attr: val}
        obj = storage.all()[key]
        obj.__dict__.update(new_attr)
        obj.save()
        
    def help_update(self):
        """docs for the update command."""
        print("updates one attribute of one object.")
        print("[usage]: update <classname> <id> <attribute name> <attribute value>")
        
    def do_quit(self, line):
        """this method defines the logic for the quit command."""
        return True

    def help_quit(self):
        """docs for the command quit"""
        print("terminates the shell.")

    def do_EOF(self, line):
        """defines the logic for EOF."""
        print()
        return True

    def help_EOF(self):
        """docs for the command EOF."""
        print("receives the EOF signal and terminates the shell.")
    
    def emptyline(self):
        """method called when the input is empty"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
