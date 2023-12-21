# TaskSatelliteGetExtension - класс
Шаблона расширения для загрузки сателлита по идентификатору задания (в т.ч.
создание виртуального сателлита), а также заполняем поля сателлита после
успешной загрузки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class TaskSatelliteGetExtension : CardGetExtension
VB __Копировать
     Public MustInherit Class TaskSatelliteGetExtension
    	Inherits CardGetExtension
C++ __Копировать
     public ref class TaskSatelliteGetExtension abstract : public CardGetExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type TaskSatelliteGetExtension = 
        class
            inherit CardGetExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardGetExtension](T_Tessa_Cards_Extensions_CardGetExtension.htm) __ TaskSatelliteGetExtension
##  __Конструкторы
[TaskSatelliteGetExtension](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[CardGetStrategy](P_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_CardGetStrategy.htm)|
Стратегия низкоуровневой загрузки карточки, используемая при загрузке
виртуального задания.  
---|---  
[CardNewStrategy](P_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_CardNewStrategy.htm)|
Стратегия низкоуровневого создания структуры карточки, используемая при
загрузке виртуального задания.  
[CardTransactionStrategy](P_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_CardTransactionStrategy.htm)|
Стратегия обеспечения блокировок для взаимодействия с основной карточкой.  
[ExtendedRepository](P_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_ExtendedRepository.htm)|
Репозиторий для управления карточками с расширениями и транзакцией.  
[ExtendedRepositoryWithoutTransaction](P_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_ExtendedRepositoryWithoutTransaction.htm)|
Репозиторий для управления карточками с расширениями, но без транзакции.  
[FileIsExternalKey](P_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_FileIsExternalKey.htm)|
Имя уникального ключа, по которому в информации по файлу сателлита file.Info
будет указан признак того, что файл виртуальный и на самом деле относится к
основной карточке. Если в файле ключ не указан, то файл относится именно к
сателлиту, т.е. это невиртуальный файл.  
[MainCardDigestInVirtualSatelliteSectionFieldName](P_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_MainCardDigestInVirtualSatelliteSectionFieldName.htm)|
Имя поля с Digest основной карточки, которое содержится в виртуальной
строковой секции в карточке-сателлите.  
[SatelliteTypeID](P_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_SatelliteTypeID.htm)|
Идентификатор типа карточки-сателлита.  
[VirtualMainCardIDKey](P_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_VirtualMainCardIDKey.htm)|
Имя уникального ключа, по которому в карточке сателлита card.Info содержится
идентификатор основной карточки, если карточка-сателлит была открыта как
виртуальная, т.е. она не существовала на момент загрузки. Если в карточке ключ
не указан, то сателлит уже был создан ранее.  
[VirtualSatelliteSection](P_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_VirtualSatelliteSection.htm)|
Имя виртуальной строковой секции в карточке-сателлите, в которой содержится
Digest основной карточки.  
## __Методы
[AfterRequest](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_AfterRequest.htm)|
Действие, выполняемое после получения карточки как при успешном, так и при
неудачном результате.  
(Переопределяет
[CardGetExtension.AfterRequest(ICardGetExtensionContext)](M_Tessa_Cards_Extensions_CardGetExtension_AfterRequest.htm))  
---|---  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardGetExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после получения
карточки как при успешном, так и при неудачном результате. Необработанные
исключения не прерывают выполнение цепочки расширений.  
(Унаследован от
[CardGetExtension](T_Tessa_Cards_Extensions_CardGetExtension.htm))  
[BeforeRequest](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_BeforeRequest.htm)|
Действие, выполняемое перед получением карточки стандартными средствами. Может
установить ответ на запрос для того, чтобы получение карточки стандартными
средствами не выполнялось.  
(Переопределяет
[CardGetExtension.BeforeRequest(ICardGetExtensionContext)](M_Tessa_Cards_Extensions_CardGetExtension_BeforeRequest.htm))  
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
[LoadExternalCardsWithFilesListAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_LoadExternalCardsWithFilesListAsync.htm)|
Возвращает идентификаторы карточек-сателлитов, которые содержат файлы и для
которых файлы требуется загрузить как виртуальные файлы для текущей карточки-
сателлита. Например, это идентификаторы сателлитов для заданий, которые
расположены выше по иерархии в истории заданий.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[PrepareRequestToLoadMainCardAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_PrepareRequestToLoadMainCardAsync.htm)|
Подготавливает запрос на загрузку основной карточки, данные которой
используются, а также информация по правам доступа к которой используются при
загрузке карточки-сателлита.  
[PrepareSatelliteAfterLoadingAndGetAdditionalInfoAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_PrepareSatelliteAfterLoadingAndGetAdditionalInfoAsync.htm)|
Выполняет постобработку загруженной карточки-сателлита, а также возвращает
дополнительную информацию, такую как токен прав доступа, которая используется
в других методах этого класса, в т.ч. для загрузки основной карточки. Если
такой информации нет, то возвращает null.  
[PrepareSatelliteWithMainCardInfoAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_PrepareSatelliteWithMainCardInfoAsync.htm)|
Подготавливает данные карточки-сателлита по данным загруженной основной
карточки.  
[SetupSatelliteFileAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_SetupSatelliteFileAsync.htm)|
Устанавливает свойства загруженного файла в карточке-сателлите для учёта того,
что файл может принадлежать основной карточке.  
[SetupVirtualSatelliteAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_SetupVirtualSatelliteAsync.htm)|
В виртуальной карточке-сателлите устанавливает идентификаторы основной
карточки и задания, к которым относится сателлит.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetMainCardIDAndTaskRowIDAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_TryGetMainCardIDAndTaskRowIDAsync.htm)|
Возвращает идентификатор основной карточки и идентификатор задания по
идентификатору карточки-сателлита. Значение false возвращается в том случае,
если сателлит не существует.  
[TryGetMainCardIDByTaskRowIDAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_TryGetMainCardIDByTaskRowIDAsync.htm)|
Возвращает идентификатор основной карточки по идентификатору задания или null,
если карточка не найдена.  
[TryGetTaskSatelliteIDAsync](M_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension_TryGetTaskSatelliteIDAsync.htm)|
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
