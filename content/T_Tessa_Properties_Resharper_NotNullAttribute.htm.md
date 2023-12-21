# NotNullAttribute - класс
Indicates that the value of the marked element could never be null
##  __Definition
 **Пространство имён:**
[Tessa.Properties.Resharper](N_Tessa_Properties_Resharper.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [AttributeUsageAttribute(AttributeTargets.Delegate|AttributeTargets.Field|AttributeTargets.Method|AttributeTargets.Parameter|AttributeTargets.Property, AllowMultiple = false, 
    	Inherited = true)]
    public sealed class NotNullAttribute : Attribute
VB __Копировать
    <AttributeUsageAttribute(AttributeTargets.Delegate Or AttributeTargets.Field Or AttributeTargets.Method Or AttributeTargets.Parameter Or AttributeTargets.Property, AllowMultiple := false, 
    	Inherited := true)>
    Public NotInheritable Class NotNullAttribute
    	Inherits Attribute
C++ __Копировать
    [AttributeUsageAttribute(AttributeTargets::Delegate|AttributeTargets::Field|AttributeTargets::Method|AttributeTargets::Parameter|AttributeTargets::Property, AllowMultiple = false, 
    	Inherited = true)]
    public ref class NotNullAttribute sealed : public Attribute
F# __Копировать
     [<SealedAttribute>]
    [<AttributeUsageAttribute(AttributeTargets.Delegate|AttributeTargets.Field|AttributeTargets.Method|AttributeTargets.Parameter|AttributeTargets.Property, AllowMultiple = false, 
    	Inherited = true)>]
    type NotNullAttribute = 
        class
            inherit Attribute
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute) __ NotNullAttribute
##  __Пример
C# __Копировать
    [NotNull]
    public object Foo()
    {
      return null; // Warning: Possible 'null' assignment
    }
##  __Конструкторы
[NotNullAttribute](M_Tessa_Properties_Resharper_NotNullAttribute__ctor.htm)|
Инициализирует новый экземпляр класса NotNullAttribute  
---|---  
##  __Свойства
[TypeId](https://learn.microsoft.com/dotnet/api/system.attribute.typeid#system-
attribute-typeid)| When implemented in a derived class, gets a unique
identifier for this
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute).  
(Унаследован от
[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute))  
---|---  
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
