# TaskSatelliteStoreExtension - класс
Шаблона расширения по сохранению карточки-сателлита для задания.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class TaskSatelliteStoreExtension : CardStoreExtension
VB __Копировать
     Public MustInherit Class TaskSatelliteStoreExtension
    	Inherits CardStoreExtension
C++ __Копировать
     public ref class TaskSatelliteStoreExtension abstract : public CardStoreExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type TaskSatelliteStoreExtension = 
        class
            inherit CardStoreExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm) __ TaskSatelliteStoreExtension
##  __Конструкторы
[TaskSatelliteStoreExtension](M_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[CardGetStrategy](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_CardGetStrategy.htm)|
Стратегия низкоуровневой загрузки карточки, используемая при загрузке
виртуального задания.  
---|---  
[CardTransactionStrategy](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_CardTransactionStrategy.htm)|
Стратегия обеспечения блокировок для взаимодействия с основной карточкой.  
[ContextCardInfoKey](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_ContextCardInfoKey.htm)|
Имя уникального ключа, по которому в контексте расширений context.Info между
методами расширений передаётся информация из сохраняемой карточки card.Info.  
[ContextFilesKey](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_ContextFilesKey.htm)|
Имя уникального ключа, по которому в контексте расширений context.Info между
методами расширений передаётся список файлов ListStorage<CardFile>.  
[ContextMainCardIDKey](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_ContextMainCardIDKey.htm)|
Имя уникального ключа, по которому в контексте расширений context.Info между
методами расширений передаётся идентификатор основной карточки.  
[ContextTasksKey](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_ContextTasksKey.htm)|
Имя уникального ключа, по которому в контексте расширений context.Info между
методами расширений передаётся список заданий ListStorage<CardTask>.  
[ExtendedRepository](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_ExtendedRepository.htm)|
Репозиторий для управления карточками с расширениями и с транзакцией.  
[ExtendedRepositoryWithoutTransaction](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_ExtendedRepositoryWithoutTransaction.htm)|
Репозиторий для управления карточками с расширениями, но без транзакции.  
[NextCardIDKey](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_NextCardIDKey.htm)|
Имя уникального ключа, по которому в ответе на запрос response.Info содержится
идентификатор карточки, которую надо открыть после сохранения сателлита. Если
в ответе на запрос ключ не указан, то после сохранения повторно открывается
сателлит.  
[NextCardTypeIDKey](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_NextCardTypeIDKey.htm)|
Имя уникального ключа, по которому в ответе на запрос response.Info содержится
идентификатор типа карточки, которую надо открыть после сохранения сателлита.
Если в ответе на запрос ключ не указан, то после сохранения повторно
открывается сателлит.  
[SatelliteTypeID](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_SatelliteTypeID.htm)|
Идентификатор типа карточки-сателлита.  
[VirtualMainCardIDKey](P_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_VirtualMainCardIDKey.htm)|
Имя уникального ключа, по которому в карточке сателлита card.Info содержится
идентификатор основной карточки, если карточка-сателлит была открыта как
виртуальная, т.е. она не существовала на момент загрузки. Если в карточке ключ
не указан, то сателлит уже был создан ранее.  
## __Методы
[AfterBeginTransaction](M_Tessa_Cards_Extensions_CardStoreExtension_AfterBeginTransaction.htm)|
Действие, выполняемое после начала транзакции.  
(Унаследован от
[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm))  
---|---  
[AfterRequest](M_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_AfterRequest.htm)|  
(Переопределяет
[CardStoreExtension.AfterRequest(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_CardStoreExtension_AfterRequest.htm))  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardStoreExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после сохранения
карточки как при успешном, так и при неудачном результате. Необработанные
исключения не прерывают выполнение цепочки расширений.  
(Унаследован от
[CardStoreExtension](T_Tessa_Cards_Extensions_CardStoreExtension.htm))  
[BeforeCommitTransaction](M_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_BeforeCommitTransaction.htm)|  
(Переопределяет
[CardStoreExtension.BeforeCommitTransaction(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_CardStoreExtension_BeforeCommitTransaction.htm))  
[BeforeRequest](M_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_BeforeRequest.htm)|  
(Переопределяет
[CardStoreExtension.BeforeRequest(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_CardStoreExtension_BeforeRequest.htm))  
[CanModifyTaskCardAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_CanModifyTaskCardAsync.htm)|
Возвращает признак того, что карточку-сателлит разрешено сохранять на
основании данных по заданию.  
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
[IsMainCardFileAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_IsMainCardFileAsync.htm)|
Возвращает признак того, что заданный файл, сохраняемый с карточкой-
сателлитом, на самом деле относится к основной карточке.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[PrepareMainCardFileToStoreAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_PrepareMainCardFileToStoreAsync.htm)|
Выполняет подготовку для заданного файла, сохраняемого с карточкой-сателлитом,
но для которого известно, что он является файлом основной карточки. Например,
устанавливается категория файла в основной карточке.  
[SetupVirtualSatelliteAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_SetupVirtualSatelliteAsync.htm)|
В виртуальной карточке-сателлите устанавливает идентификаторы основной
карточки и задания, к которым относится сателлит.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetMainCardIDAndTaskRowIDAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_TryGetMainCardIDAndTaskRowIDAsync.htm)|
Возвращает идентификатор основной карточки и идентификатор задания по
идентификатору карточки-сателлита. Значение false возвращается в том случае,
если сателлит не существует.  
[TryGetTaskSatelliteIDAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension_TryGetTaskSatelliteIDAsync.htm)|
Возвращает идентификатор карточки-сателлита по идентификатору задания на
основании данных в базе данных или null, если сателлит не существует.  
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
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
