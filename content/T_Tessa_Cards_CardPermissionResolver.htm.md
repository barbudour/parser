# CardPermissionResolver - класс
Осуществляет поиск прав доступа для полей, строк, файлов и карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardPermissionResolver : ICardPermissionResolver
VB __Копировать
     Public NotInheritable Class CardPermissionResolver
    	Implements ICardPermissionResolver
C++ __Копировать
     public ref class CardPermissionResolver sealed : ICardPermissionResolver
F# __Копировать
     [<SealedAttribute>]
    type CardPermissionResolver = 
        class
            interface ICardPermissionResolver
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardPermissionResolver
Implements
    [ICardPermissionResolver](T_Tessa_Cards_ICardPermissionResolver.htm)
##  __Конструкторы
[CardPermissionResolver](M_Tessa_Cards_CardPermissionResolver__ctor.htm)|
Создаёт экземпляр класса с указанием объекта, содержащего права доступа на
карточку и её секции.  
---|---  
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
[GetCardPermissions](M_Tessa_Cards_CardPermissionResolver_GetCardPermissions.htm)|
Возвращает права доступа к карточке.  
[GetFieldPermissions(String,
String)](M_Tessa_Cards_CardPermissionResolver_GetFieldPermissions.htm)|
Возвращает права доступа к полю fieldName из секции sectionName.  
[GetFieldPermissions(String, String,
Guid)](M_Tessa_Cards_CardPermissionResolver_GetFieldPermissions_1.htm)|
Возвращает права доступа к полю fieldName из коллекционной или древовидной
секции sectionName и строки с идентификатором rowID.  
[GetFilePermissions](M_Tessa_Cards_CardPermissionResolver_GetFilePermissions.htm)|
Возвращает права доступа к прикреплённому к карточке файлу fileID.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetRowPermissions](M_Tessa_Cards_CardPermissionResolver_GetRowPermissions.htm)|
Возвращает права доступа к строке с идентификатором rowID из секции
sectionName.  
[GetSectionPermissions](M_Tessa_Cards_CardPermissionResolver_GetSectionPermissions.htm)|
Возвращает права доступа к строкам или полям секции sectionName.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Invalidate](M_Tessa_Cards_CardPermissionResolver_Invalidate.htm)|
Очищает кэш прав доступа.
Метод необходимо вызывать всякий раз перед поиском прав доступа, если нет
уверенности в неизменности прав доступа после предыдущего поиска.  
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
[GetEntryPermissions](M_Tessa_Cards_CardExtensions_GetEntryPermissions.htm)|
Возвращает права доступа к полям строковой секции с именем sectionName.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[GetTablePermissions](M_Tessa_Cards_CardExtensions_GetTablePermissions.htm)|
Возвращает права доступа к строкам коллекционной секции с именем sectionName.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
