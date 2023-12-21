# NotifyPropertyChangedInvocatorAttribute - класс
Indicates that the method is contained in a type that implements
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged)
interface and this method is used to notify that some property value changed.
## __Definition
 **Пространство имён:**
[Tessa.Properties.Resharper](N_Tessa_Properties_Resharper.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [AttributeUsageAttribute(AttributeTargets.Method, AllowMultiple = false, Inherited = true)]
    public sealed class NotifyPropertyChangedInvocatorAttribute : Attribute
VB __Копировать
    <AttributeUsageAttribute(AttributeTargets.Method, AllowMultiple := false, Inherited := true)>
    Public NotInheritable Class NotifyPropertyChangedInvocatorAttribute
    	Inherits Attribute
C++ __Копировать
    [AttributeUsageAttribute(AttributeTargets::Method, AllowMultiple = false, Inherited = true)]
    public ref class NotifyPropertyChangedInvocatorAttribute sealed : public Attribute
F# __Копировать
     [<SealedAttribute>]
    [<AttributeUsageAttribute(AttributeTargets.Method, AllowMultiple = false, Inherited = true)>]
    type NotifyPropertyChangedInvocatorAttribute = 
        class
            inherit Attribute
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute) __ NotifyPropertyChangedInvocatorAttribute
##  __Заметки
The method should be non-static and conform to one of the supported
signatures:
  * NotifyChanged(string)
  * NotifyChanged(params string[])
  * NotifyChanged{T}(Expression{Func{T}})
  * NotifyChanged{T,U}(Expression{Func{T,U}})
  * SetProperty{T}(ref T, T, string)
##  __Пример
C# __Копировать
     public class Foo : INotifyPropertyChanged
    {
      public event PropertyChangedEventHandler PropertyChanged;
      [NotifyPropertyChangedInvocator]
      protected virtual void NotifyChanged(string propertyName)
      {}
      private string _name;
      public string Name
      {
        get { return _name; }
        set
        {
          _name = value;
          NotifyChanged("LastName"); // Warning
        }
      }
    }
Examples of generated notifications:
  * NotifyChanged("Property")
  * NotifyChanged(() => Property)
  * NotifyChanged((VM x) => x.Property)
  * SetProperty(ref myField, value, "Property")
##  __Конструкторы
[NotifyPropertyChangedInvocatorAttribute()](M_Tessa_Properties_Resharper_NotifyPropertyChangedInvocatorAttribute__ctor.htm)|
Initializes a new instance of the NotifyPropertyChangedInvocatorAttribute
class.  
---|---  
[NotifyPropertyChangedInvocatorAttribute(String)](M_Tessa_Properties_Resharper_NotifyPropertyChangedInvocatorAttribute__ctor_1.htm)|
Initializes a new instance of the NotifyPropertyChangedInvocatorAttribute
class.  
## __Свойства
[ParameterName](P_Tessa_Properties_Resharper_NotifyPropertyChangedInvocatorAttribute_ParameterName.htm)|
Gets the parameter name.  
---|---  
[TypeId](https://learn.microsoft.com/dotnet/api/system.attribute.typeid#system-
attribute-typeid)| When implemented in a derived class, gets a unique
identifier for this
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute).  
(Унаследован от
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute))  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.attribute.equals#system-
attribute-equals\(system-object\))| Returns a value that indicates whether
this instance is equal to a specified object.  
(Унаследован от
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.attribute.gethashcode#system-
attribute-gethashcode)| Returns the hash code for this instance.  
(Унаследован от
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsDefaultAttribute](https://learn.microsoft.com/dotnet/api/system.attribute.isdefaultattribute#system-
attribute-isdefaultattribute)| When overridden in a derived class, indicates
whether the value of this instance is the default value for the derived class.  
(Унаследован от
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute))  
[Match](https://learn.microsoft.com/dotnet/api/system.attribute.match#system-
attribute-match\(system-object\))| When overridden in a derived class, returns
a value that indicates whether this instance equals a specified object.  
(Унаследован от
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Properties.Resharper - пространство
имён](N_Tessa_Properties_Resharper.htm)
