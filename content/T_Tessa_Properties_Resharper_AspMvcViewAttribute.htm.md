# AspMvcViewAttribute - класс
ASP.NET MVC attribute. If applied to a parameter, indicates that the parameter
is an MVC view. If applied to a method, the MVC view name is calculated
implicitly from the context. Use this attribute for custom wrappers similar to
System.Web.Mvc.Controller.View(Object)"
##  __Definition
 **Пространство имён:**
[Tessa.Properties.Resharper](N_Tessa_Properties_Resharper.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [AttributeUsageAttribute(AttributeTargets.Method|AttributeTargets.Parameter)]
    public sealed class AspMvcViewAttribute : PathReferenceAttribute
VB __Копировать
    <AttributeUsageAttribute(AttributeTargets.Method Or AttributeTargets.Parameter)>
    Public NotInheritable Class AspMvcViewAttribute
    	Inherits PathReferenceAttribute
C++ __Копировать
    [AttributeUsageAttribute(AttributeTargets::Method|AttributeTargets::Parameter)]
    public ref class AspMvcViewAttribute sealed : public PathReferenceAttribute
F# __Копировать
     [<SealedAttribute>]
    [<AttributeUsageAttribute(AttributeTargets.Method|AttributeTargets.Parameter)>]
    type AspMvcViewAttribute = 
        class
            inherit PathReferenceAttribute
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute) __[PathReferenceAttribute](T_Tessa_Properties_Resharper_PathReferenceAttribute.htm) __ AspMvcViewAttribute
##  __Конструкторы
[AspMvcViewAttribute](M_Tessa_Properties_Resharper_AspMvcViewAttribute__ctor.htm)|
Инициализирует новый экземпляр класса AspMvcViewAttribute  
---|---  
##  __Свойства
[BasePath](P_Tessa_Properties_Resharper_PathReferenceAttribute_BasePath.htm)|
Gets the base path.  
(Унаследован от
[PathReferenceAttribute](T_Tessa_Properties_Resharper_PathReferenceAttribute.htm))  
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
