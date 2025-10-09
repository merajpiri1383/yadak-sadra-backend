from django.contrib.auth.base_user import BaseUserManager


class UserManager (BaseUserManager) : 

    def create_user (self,username,phone,password=None,**kwargs) : 
        user = self.model(username=username,phone=phone,**kwargs)
        if password : 
            user.set_password(password)
        user.save()
        return user
    
    def create_superuser (self,username,phone,password=None,**kwargs) : 
        kwargs.setdefault("is_active",True)
        kwargs.setdefault("is_staff",True)
        kwargs.setdefault("is_superuser",True)
        
        if not kwargs.get("is_active") : 
            raise ValueError("is_active must be true .")
        
        if not kwargs.get("is_staff") : 
            raise ValueError("is_staff must be true .")
        
        if not kwargs.get("is_superuser") : 
            raise ValueError("is_superuser must be true .")
        
        return self.create_user(username,phone,password,**kwargs)