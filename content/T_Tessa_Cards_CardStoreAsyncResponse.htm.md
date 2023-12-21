# CardStoreAsyncResponse - класс
Объект, предоставляющий доступ к результату асинхронной операции по сохранению
карточки с файлами.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardStoreAsyncResponse : ICardStoreAsyncResponse
VB __Копировать
     Public NotInheritable Class CardStoreAsyncResponse
    	Implements ICardStoreAsyncResponse
C++ __Копировать
     public ref class CardStoreAsyncResponse sealed : ICardStoreAsyncResponse
F# __Копировать
     [<SealedAttribute>]
    type CardStoreAsyncResponse = 
        class
            interface ICardStoreAsyncResponse
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardStoreAsyncResponse
Implements
    [ICardStoreAsyncResponse](T_Tessa_Cards_ICardStoreAsyncResponse.htm)
##  __Конструкторы
[CardStoreAsyncResponse](M_Tessa_Cards_CardStoreAsyncResponse__ctor.htm)|
Создаёт экземпляр класса с указанием асинхронной операции по сохранению
карточки с файлами и функции, возвращающей общее количество байт, относящихся
к файлам, которое было загружено на сервер.  
---|---  
## __Свойства
[Empty](P_Tessa_Cards_CardStoreAsyncResponse_Empty.htm)|  Объект,
представляющий отсутствующий результат асинхронной операции по сохранению
карточки с файлами. Свойство
[Task](P_Tessa_Cards_CardStoreAsyncResponse_Task.htm) возвращает незапущенное
задание, а другие свойства всегда возвращают 0.  
---|---  
[FileProgress](P_Tessa_Cards_CardStoreAsyncResponse_FileProgress.htm)|
Прогресс операции, вычисляемый как отношение суммарного количества уже
загруженных байт, относящихся к файлам, к суммарному размеру всех файлов,
которые требуется загрузить. Не учитывает размеры заголовка и запроса на
сохранение карточки.  
[Task](P_Tessa_Cards_CardStoreAsyncResponse_Task.htm)| Асинхронная операция по
сохранению карточки с файлами.  
[TotalFileLength](P_Tessa_Cards_CardStoreAsyncResponse_TotalFileLength.htm)|
Суммарное количество байт, относящихся к файлам, которое будет загружено на
сервер. Не включает в себя размеры заголовка и запроса на сохранение карточки.  
[UploadedFileLength](P_Tessa_Cards_CardStoreAsyncResponse_UploadedFileLength.htm)|
Суммарное количество байт, относящихся к файлам, которое было загружено на
сервер. Не включает в себя размеры заголовка и запроса на сохранение карточки.  
## __Методы
[ConfigureAwait](M_Tessa_Cards_CardStoreAsyncResponse_ConfigureAwait.htm)|
Настраивает ожидание задачи.  
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
[GetAwaiter](M_Tessa_Cards_CardStoreAsyncResponse_GetAwaiter.htm)|  Возвращает
объект, выполняющий ожидание результата задачи [ICardStoreAsyncResponse.Task].  
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
