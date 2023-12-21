# SessionMethodAttribute - класс
Указывает, что метод поддерживает сессию Tessa для проверки доступа и для
передачи информации о клиенте.
## __Definition
 **Пространство имён:** [Tessa.Web](N_Tessa_Web.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
    [AttributeUsageAttribute(AttributeTargets.Class|AttributeTargets.Method)]
    public sealed class SessionMethodAttribute : Attribute, 
    	IAsyncActionFilter, IFilterMetadata
VB __Копировать
    <AttributeUsageAttribute(AttributeTargets.Class Or AttributeTargets.Method)>
    Public NotInheritable Class SessionMethodAttribute
    	Inherits Attribute
    	Implements IAsyncActionFilter, IFilterMetadata
C++ __Копировать
    [AttributeUsageAttribute(AttributeTargets::Class|AttributeTargets::Method)]
    public ref class SessionMethodAttribute sealed : public Attribute, 
    	IAsyncActionFilter, IFilterMetadata
F# __Копировать
     [<SealedAttribute>]
    [<AttributeUsageAttribute(AttributeTargets.Class|AttributeTargets.Method)>]
    type SessionMethodAttribute = 
        class
            inherit Attribute
            interface IAsyncActionFilter
            interface IFilterMetadata
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Attribute](https://learn.microsoft.com/dotnet/api/system.attribute) __ SessionMethodAttribute
Implements
    [IAsyncActionFilter](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.filters.iasyncactionfilter), [IFilterMetadata](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.filters.ifiltermetadata)
##  __Конструкторы
[SessionMethodAttribute](M_Tessa_Web_SessionMethodAttribute__ctor.htm)|
Указывает, что метод поддерживает сессию Tessa для проверки доступа и для
передачи информации о клиенте.  
---|---  
## __Свойства
[AccessLevel](P_Tessa_Web_SessionMethodAttribute_AccessLevel.htm)|  Требуемый
уровень доступа пользователя.  
---|---  
[OperationFullName](P_Tessa_Web_SessionMethodAttribute_OperationFullName.htm)|
Полное имя текущей операции, включающее информацию по сервису/контроллеру и
собственно операции. Имя может использоваться при логировании. Значение по
умолчанию null определяет, что имя операции будет определено автоматически из
запрошенного маршрута.  
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
[OnActionExecutionAsync](M_Tessa_Web_SessionMethodAttribute_OnActionExecutionAsync.htm)|  
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
[Tessa.Web - пространство имён](N_Tessa_Web.htm)