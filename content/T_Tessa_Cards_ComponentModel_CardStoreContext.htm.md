# CardStoreContext - класс
Контекст операции по сохранению карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardStoreContext
VB __Копировать
     Public NotInheritable Class CardStoreContext
C++ __Копировать
     public ref class CardStoreContext sealed
F# __Копировать
     [<SealedAttribute>]
    type CardStoreContext = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardStoreContext
##  __Конструкторы
[CardStoreContext](M_Tessa_Cards_ComponentModel_CardStoreContext__ctor.htm)|
Создаёт экземпляр класса с указанием информации, требуемой для сохранения
карточки. Рассмотрите использование статического метода [CreateAsync(Card,
DateTime, ISession, ICardMetadata, IValidationResultBuilder, IQueryExecutor,
IQueryBuilderFactory, Boolean, CardStoreMethod,
CancellationToken)](M_Tessa_Cards_ComponentModel_CardStoreContext_CreateAsync.htm)
для упрощённого создания экземпляра объекта.  
---|---  
## __Свойства
[AffectModified](P_Tessa_Cards_ComponentModel_CardStoreContext_AffectModified.htm)|
Признак того, что изменения влияют на изменение информации по тому, когда
произошло изменение карточки и какой пользователь его выполнил. Это поле
эффективно только в случае, если значение свойства
[AffectVersion](P_Tessa_Cards_ComponentModel_CardStoreContext_AffectVersion.htm)
равно false.  
---|---  
[AffectVersion](P_Tessa_Cards_ComponentModel_CardStoreContext_AffectVersion.htm)|
Признак того, что изменения влияют на проверку и инкремент версии карточки.
При инкременте версии также изменяется информация по тому, когда произошло
изменение карточки и какой пользователь его выполнил. Этот флаг менее
приоритетный, чем
[DoesNotAffectVersion](P_Tessa_Cards_ComponentModel_CardStoreContext_DoesNotAffectVersion.htm).  
[BuilderFactory](P_Tessa_Cards_ComponentModel_CardStoreContext_BuilderFactory.htm)|
Объект, помогающий создавать SQL-команды для сохранению карточки.  
[CancellationToken](P_Tessa_Cards_ComponentModel_CardStoreContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
[CardID](P_Tessa_Cards_ComponentModel_CardStoreContext_CardID.htm)|
Идентификатор сохраняемой карточки.  
[CardMetadata](P_Tessa_Cards_ComponentModel_CardStoreContext_CardMetadata.htm)|
Метаинформация по типу сохраняемой карточки.  
[CardTypeCaption](P_Tessa_Cards_ComponentModel_CardStoreContext_CardTypeCaption.htm)|
Отображаемое имя типа сохраняемой карточки.  
[CardTypeID](P_Tessa_Cards_ComponentModel_CardStoreContext_CardTypeID.htm)|
Идентификатор типа сохраняемой карточки.  
[DoesNotAffectVersion](P_Tessa_Cards_ComponentModel_CardStoreContext_DoesNotAffectVersion.htm)|
Признак того, что изменение карточки не приведёт к проверке и к увеличению
номера версии, даже если присутствуют изменяемые значения в основной карточке
или её файлах. При первом сохранении карточки версия всё равно увеличивается
до 1. Этот флаг более приоритетный, чем
[AffectVersion](P_Tessa_Cards_ComponentModel_CardStoreContext_AffectVersion.htm).  
[ExcludedQueryCount](P_Tessa_Cards_ComponentModel_CardStoreContext_ExcludedQueryCount.htm)|
Количество запросов, выполненных через
[Executor](P_Tessa_Cards_ComponentModel_CardStoreContext_Executor.htm),
которые не учитываются в стандартном API при определении того, следует ли
выполнять проверку и инкремент версии карточки.  
[Executor](P_Tessa_Cards_ComponentModel_CardStoreContext_Executor.htm)|
Объект, выполняющий SQL-команды по сохранению карточки.  
[Files](P_Tessa_Cards_ComponentModel_CardStoreContext_Files.htm)|  Файлы
сохраняемой карточки.  
[ForceTransaction](P_Tessa_Cards_ComponentModel_CardStoreContext_ForceTransaction.htm)|
Признак того, что будет открыта транзакция независимо от наличия изменений в
карточке.  
[GeneralMetadata](P_Tessa_Cards_ComponentModel_CardStoreContext_GeneralMetadata.htm)|
Общая метаинформация по типам карточек.  
[HasUserInfo](P_Tessa_Cards_ComponentModel_CardStoreContext_HasUserInfo.htm)|
Признак того, что в контексте присутствует действительная информация об имени
и идентификаторе пользователя, выполняющего сохранение карточки. При
отсутствии карточки сохранение должно выполняться от имени пользователя
System.  
[RepairSections](P_Tessa_Cards_ComponentModel_CardStoreContext_RepairSections.htm)|
Флаг указывает на то, что нужно починить (добавить) строковые секции карточки
в случае, если они отсутствуют в БД.  
[Sections](P_Tessa_Cards_ComponentModel_CardStoreContext_Sections.htm)|
Секции сохраняемой карточки.  
[Session](P_Tessa_Cards_ComponentModel_CardStoreContext_Session.htm)|  Сессия
текущего пользователя.  
[StoreDateTime](P_Tessa_Cards_ComponentModel_CardStoreContext_StoreDateTime.htm)|
Время сохранения карточки в формате UTC.  
[StoreMethod](P_Tessa_Cards_ComponentModel_CardStoreContext_StoreMethod.htm)|
Специализация для способа сохранения карточки.  
[StoreMode](P_Tessa_Cards_ComponentModel_CardStoreContext_StoreMode.htm)|
Способ сохранения карточки.  
[TaskHistory](P_Tessa_Cards_ComponentModel_CardStoreContext_TaskHistory.htm)|
История заданий сохраняемой карточки  
[TaskHistoryGroups](P_Tessa_Cards_ComponentModel_CardStoreContext_TaskHistoryGroups.htm)|
Группы истории заданий сохраняемой карточки  
[TaskRowIDListToMakeInProgress](P_Tessa_Cards_ComponentModel_CardStoreContext_TaskRowIDListToMakeInProgress.htm)|
Список идентификаторов заданий, которые берутся в работу в процессе
сохранения. Для каждого такого задания выполняются дополнительные проверки
внутри блокировки на запись карточки.  
[Tasks](P_Tessa_Cards_ComponentModel_CardStoreContext_Tasks.htm)|  Задания
сохраняемой карточки.  
[UserID](P_Tessa_Cards_ComponentModel_CardStoreContext_UserID.htm)|
Идентификатор пользователя, выполняющего сохранение карточки.  
[UserName](P_Tessa_Cards_ComponentModel_CardStoreContext_UserName.htm)|  Имя
пользователя, выполняющего сохранение карточки.  
[ValidationResult](P_Tessa_Cards_ComponentModel_CardStoreContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации.  
## __Методы
[CreateAsync](M_Tessa_Cards_ComponentModel_CardStoreContext_CreateAsync.htm)|
Создаёт экземпляр класса с указанием информации, требуемой для сохранения
заданной карточки [Card](T_Tessa_Cards_Card.htm).  
---|---  
[CreateForAsync](M_Tessa_Cards_ComponentModel_CardStoreContext_CreateForAsync.htm)|
Создаёт контекст операции по сохранению карточки, которая вложена в текущую
карточку. Это может быть карточка файла или задания.  
[DeferDeletionAction](M_Tessa_Cards_ComponentModel_CardStoreContext_DeferDeletionAction.htm)|
Откладывает выполнение действия по удалению элемента карточки.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExecuteDeferredDeletionActionsInReversedOrderAsync](M_Tessa_Cards_ComponentModel_CardStoreContext_ExecuteDeferredDeletionActionsInReversedOrderAsync.htm)|
Осуществляет отложенное выполнение всех действий по удалению элементов
карточки в порядке, обратном их указанию.  
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
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
