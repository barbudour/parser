# KrUniversalTaskStoreExtension - класс
Расширение на сохранение задания
[KrUniversalTaskTypeID](F_Tessa_Extensions_Default_Shared_DefaultTaskTypes_KrUniversalTaskTypeID.htm).
Сохраняет вариант завершения задания, с которым оно было завершено, и
комментарий в [Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm). Завершает
задание с вариантом завершения
[Approve](F_Tessa_Extensions_Default_Shared_DefaultCompletionOptions_Approve.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess](N_Tessa_Extensions_Default_Server_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrUniversalTaskStoreExtension : CardStoreTaskExtension
VB __Копировать
     Public NotInheritable Class KrUniversalTaskStoreExtension
    	Inherits CardStoreTaskExtension
C++ __Копировать
     public ref class KrUniversalTaskStoreExtension sealed : public CardStoreTaskExtension
F# __Копировать
     [<SealedAttribute>]
    type KrUniversalTaskStoreExtension = 
        class
            inherit CardStoreTaskExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardStoreTaskExtension](T_Tessa_Cards_Extensions_CardStoreTaskExtension.htm) __ KrUniversalTaskStoreExtension
##  __Конструкторы
[KrUniversalTaskStoreExtension](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrUniversalTaskStoreExtension__ctor.htm)|
Инициализирует новый экземпляр класса KrUniversalTaskStoreExtension  
---|---  
##  __Методы
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
[StoreTaskAfterBeginTransaction](M_Tessa_Cards_Extensions_CardStoreTaskExtension_StoreTaskAfterBeginTransaction.htm)|
Действие, выполняемое после начала транзакции на сохранение задания, которое
включает в себя создание, изменение, завершение и удаление. Метод выполняется
всегда, если был выполнен метод
[Tessa.Cards.Extensions.ICardStoreTaskExtension.StoreTaskBeforeRequest].  
(Унаследован от
[CardStoreTaskExtension](T_Tessa_Cards_Extensions_CardStoreTaskExtension.htm))  
[StoreTaskAfterRequest](M_Tessa_Cards_Extensions_CardStoreTaskExtension_StoreTaskAfterRequest.htm)|
Действие, выполняемое после сохранения задания, которое включает в себя
создание, изменение, завершение и удаление. Метод выполняется всегда, если был
выполнен метод
[Tessa.Cards.Extensions.ICardStoreTaskExtension.StoreTaskBeforeRequest].
Проверить, было ли сохранение задания успешным, можно, обратившись к свойству
[Tessa.Cards.Extensions.ICardExtensionContext.RequestIsSuccessful].  
(Унаследован от
[CardStoreTaskExtension](T_Tessa_Cards_Extensions_CardStoreTaskExtension.htm))  
[StoreTaskAfterRequestFinally](M_Tessa_Cards_Extensions_CardStoreTaskExtension_StoreTaskAfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после сохранения
задания (которое включает в себя создание, изменение, завершение и удаление)
как при успешном, так и при неудачном результате. Необработанные исключения не
прерывают выполнение цепочки расширений. Метод выполняется всегда, если был
выполнен метод
[Tessa.Cards.Extensions.ICardStoreTaskExtension.StoreTaskBeforeRequest].
Проверить, было ли сохранение задания успешным, можно, обратившись к свойству
[Tessa.Cards.Extensions.ICardExtensionContext.RequestIsSuccessful].  
(Унаследован от
[CardStoreTaskExtension](T_Tessa_Cards_Extensions_CardStoreTaskExtension.htm))  
[StoreTaskBeforeCommitTransaction](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrUniversalTaskStoreExtension_StoreTaskBeforeCommitTransaction.htm)|
Действие, выполняемое перед завершением транзакции на сохранение задания,
которое включает в себя создание, изменение, завершение и удаление. Метод
выполняется всегда, если был выполнен метод
[Tessa.Cards.Extensions.ICardStoreTaskExtension.StoreTaskBeforeRequest].  
(Переопределяет
[CardStoreTaskExtension.StoreTaskBeforeCommitTransaction(ICardStoreTaskExtensionContext)](M_Tessa_Cards_Extensions_CardStoreTaskExtension_StoreTaskBeforeCommitTransaction.htm))  
[StoreTaskBeforeRequest](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrUniversalTaskStoreExtension_StoreTaskBeforeRequest.htm)|
Действие, выполняемое при сохранении задания, которое включает в себя
создание, изменение, завершение и удаление.  
(Переопределяет
[CardStoreTaskExtension.StoreTaskBeforeRequest(ICardStoreTaskExtensionContext)](M_Tessa_Cards_Extensions_CardStoreTaskExtension_StoreTaskBeforeRequest.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[OptionCaptionKey](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrUniversalTaskStoreExtension_OptionCaptionKey.htm)|
Имя ключа, по которому в [Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm)
объекта настраиваемого задания содержится отображаемое имя варианта завершения
или значение null, если задание не завершается. Тип значения:
[String](https://learn.microsoft.com/dotnet/api/system.string).  
---|---  
[OptionIDKey](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrUniversalTaskStoreExtension_OptionIDKey.htm)|
Имя ключа, по которому в [Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm)
объекта настраиваемого задания содержится идентификатор варианта завершения
или значение null, если задание не завершается. Тип значения:
[Nullable<T>](https://learn.microsoft.com/dotnet/api/system.nullable-1), где T
- [Guid](https://learn.microsoft.com/dotnet/api/system.guid).  
## __Методы расширения
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess.htm)
