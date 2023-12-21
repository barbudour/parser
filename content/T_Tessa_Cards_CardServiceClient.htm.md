# CardServiceClient - класс
Сервис для управления карточками, доступный на клиенте.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardServiceClient : ICardService
VB __Копировать
     Public NotInheritable Class CardServiceClient
    	Implements ICardService
C++ __Копировать
     public ref class CardServiceClient sealed : ICardService
F# __Копировать
     [<SealedAttribute>]
    type CardServiceClient = 
        class
            interface ICardService
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardServiceClient
Implements
    [ICardService](T_Tessa_Cards_ICardService.htm)
##  __Конструкторы
[CardServiceClient](M_Tessa_Cards_CardServiceClient__ctor.htm)|  Создаёт
экземпляр класса с указанием его зависимостей.  
---|---  
## __Методы
[DeleteAsync](M_Tessa_Cards_CardServiceClient_DeleteAsync.htm)| Удаляет
карточку по информации, переданной в запросе.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetAsync](M_Tessa_Cards_CardServiceClient_GetAsync.htm)| Возвращает данные
карточки по заданному запросу.  
[GetFileContentAsync](M_Tessa_Cards_CardServiceClient_GetFileContentAsync.htm)|
Получает контент версии файла.  
[GetFileVersionsAsync](M_Tessa_Cards_CardServiceClient_GetFileVersionsAsync.htm)|
Возвращает информацию о версиях файла по заданному запросу.  
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
[NewAsync](M_Tessa_Cards_CardServiceClient_NewAsync.htm)| Возвращает
заполненную структуру карточки по заданному запросу. Физически карточка не
создаётся.  
[RequestAsync](M_Tessa_Cards_CardServiceClient_RequestAsync.htm)| Выполняет
универсальный запрос к сервису карточек.  
[StoreAsync(CardStoreRequest,
CancellationToken)](M_Tessa_Cards_CardServiceClient_StoreAsync_1.htm)|
Сохраняет карточку, переданную в запросе.  
[StoreAsync(Stream,
CancellationToken)](M_Tessa_Cards_CardServiceClient_StoreAsync.htm)| Сохраняет
карточку и её файлы, переданные в потоке карточки.  
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
