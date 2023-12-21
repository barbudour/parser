# Link - класс
Ссылка, разобранная на составные части.
## __Definition
 **Пространство имён:** [Tessa.Platform.Links](N_Tessa_Platform_Links.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class Link : ILink
VB __Копировать
     Public NotInheritable Class Link
    	Implements ILink
C++ __Копировать
     public ref class Link sealed : ILink
F# __Копировать
     [<SealedAttribute>]
    type Link = 
        class
            interface ILink
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ Link
Implements
    [ILink](T_Tessa_Platform_Links_ILink.htm)
##  __Конструкторы
[Link](M_Tessa_Platform_Links_Link__ctor.htm)|  Создаёт экземпляр класса с
указанием значений его свойств.  
---|---  
## __Свойства
[ApplicationAlias](P_Tessa_Platform_Links_Link_ApplicationAlias.htm)|  Алиас
приложения. Значение не равно null или пустой строке.  
---|---  
[Arguments](P_Tessa_Platform_Links_Link_Arguments.htm)|  Аргументы ссылки с
указанием названия действия и его параметров. Могут быть равны null или пустой
строке, если аргументы не указаны.  
[HasArguments](P_Tessa_Platform_Links_Link_HasArguments.htm)| Признак того,
что в ссылке заданы аргументы ссылки.  
[HasServerCode](P_Tessa_Platform_Links_Link_HasServerCode.htm)| Признак того,
что в ссылке задан код сервера.  
[InstanceName](P_Tessa_Platform_Links_Link_InstanceName.htm)|  Имя экземпляра
сервера. Значение не равно null или пустой строке.  
[ServerCode](P_Tessa_Platform_Links_Link_ServerCode.htm)|  Код сервера. Может
быть равен null или пустой строке, если код не указан.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Tessa.Platform.Links - пространство имён](N_Tessa_Platform_Links.htm)
