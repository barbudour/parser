# CardStoreStrategy - класс
Стратегия сохранения карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardStoreStrategy : ICardStoreStrategy
VB __Копировать
     Public NotInheritable Class CardStoreStrategy
    	Implements ICardStoreStrategy
C++ __Копировать
     public ref class CardStoreStrategy sealed : ICardStoreStrategy
F# __Копировать
     [<SealedAttribute>]
    type CardStoreStrategy = 
        class
            interface ICardStoreStrategy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardStoreStrategy
Implements
    [ICardStoreStrategy](T_Tessa_Cards_ComponentModel_ICardStoreStrategy.htm)
##  __Конструкторы
[CardStoreStrategy](M_Tessa_Cards_ComponentModel_CardStoreStrategy__ctor.htm)|
Создаёт экземпляр класса с указанием стратегии, требуемой для сохранения
карточки.  
---|---  
## __Методы
[CheckContextDataAsync](M_Tessa_Cards_ComponentModel_CardStoreStrategy_CheckContextDataAsync.htm)|
Выполняет проверки в базе данных по информации, сохранённой в контексте.
Например, проверяет, что задания, которые берутся в работу, фактически ещё не
были взяты в работу и не были завершены. Рекомендуется выполнять внутри
блокировки на запись карточки перед любыми действиями, связанными с изменением
данных. Возвращает признак того, что все проверки выполнены успешно. Если
метод возвращает false, то рекомендуется прервать сохранение карточки.  
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
[ModifyInstanceAsync](M_Tessa_Cards_ComponentModel_CardStoreStrategy_ModifyInstanceAsync.htm)|
Устанавливает информацию по дате и времени изменения карточки, и по
пользователю, который изменил карточку. Также увеличивает версию карточку,
если параметр incrementVersion равен true.  
[MoveFilesAndSetTaskAsync](M_Tessa_Cards_ComponentModel_CardStoreStrategy_MoveFilesAndSetTaskAsync.htm)|
Перемещает записи в секции по файлам из карточки с идентификатором
sourceCardID в карточку с идентификатором targetCardID с изменением ссылки на
задание targetTaskID. При этом контент файлов не перемещается между
карточками, для этого используйте метод
[Tessa.Cards.ComponentModel.ICardContentStrategy.MoveFiles].  
[MoveFilesAsync](M_Tessa_Cards_ComponentModel_CardStoreStrategy_MoveFilesAsync.htm)|
Перемещает записи в секции по файлам из карточки с идентификатором
sourceCardID в карточку с идентификатором targetCardID. При этом контент
файлов не перемещается между карточками, для этого используйте метод
[Tessa.Cards.ComponentModel.ICardContentStrategy.MoveFiles].  
[StoreAsync](M_Tessa_Cards_ComponentModel_CardStoreStrategy_StoreAsync.htm)|
Сохраняет карточку, данные её секций, файлы и задания.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetCardTypeIDAsync](M_Tessa_Cards_ComponentModel_CardStoreStrategy_TryGetCardTypeIDAsync.htm)|
Возвращает идентификатор типа карточки или null, если карточка с заданным
идентификатором уже существует.  
[TryGetTemporaryRolesAsync](M_Tessa_Cards_ComponentModel_CardStoreStrategy_TryGetTemporaryRolesAsync.htm)|
Заполняет в карточке отсутствующую информацию по временным ролям, на которые
назначены сохраняемые задания, а именно имена этих ролей, а также по авторам
задания, а именно по идентификатору, имени и должности автора. Возвращает
список временных ролей, которые требуется заполнить и добавить в процессе
сохранения карточки, или null, если при формировании списка произошли ошибки и
выполнение следует прервать.  
[UpdateOriginalTaskInfoAsync](M_Tessa_Cards_ComponentModel_CardStoreStrategy_UpdateOriginalTaskInfoAsync.htm)|
Заполняет в заданиях информацию по текущим ролям, на которые были назначены
задания, из базы данных, если это актуально для текущего сохранения (например,
если роль изменяется в процессе сохранения).  
[UpdateTaskPlannedAsync](M_Tessa_Cards_ComponentModel_CardStoreStrategy_UpdateTaskPlannedAsync.htm)|
Заполняет в заданиях информацию о плановом завершении на основании срока,
указанного в задании.  
[UpdateTimeZoneTaskInfoAsync](M_Tessa_Cards_ComponentModel_CardStoreStrategy_UpdateTimeZoneTaskInfoAsync.htm)|
Заполняет в заданиях информацию по временныс зонам.  
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
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
