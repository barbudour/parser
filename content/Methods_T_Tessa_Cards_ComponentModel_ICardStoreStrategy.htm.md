# ICardStoreStrategy - методы
##  __Методы
[CheckContextDataAsync](M_Tessa_Cards_ComponentModel_ICardStoreStrategy_CheckContextDataAsync.htm)|
Выполняет проверки в базе данных по информации, сохранённой в контексте.
Например, проверяет, что задания, которые берутся в работу, фактически ещё не
были взяты в работу и не были завершены. Рекомендуется выполнять внутри
блокировки на запись карточки перед любыми действиями, связанными с изменением
данных. Возвращает признак того, что все проверки выполнены успешно. Если
метод возвращает false, то рекомендуется прервать сохранение карточки.  
---|---  
[ModifyInstanceAsync](M_Tessa_Cards_ComponentModel_ICardStoreStrategy_ModifyInstanceAsync.htm)|
Устанавливает информацию по дате и времени изменения карточки, и по
пользователю, который изменил карточку. Также увеличивает версию карточку,
если параметр incrementVersion равен true.  
[MoveFilesAndSetTaskAsync](M_Tessa_Cards_ComponentModel_ICardStoreStrategy_MoveFilesAndSetTaskAsync.htm)|
Перемещает записи в секции по файлам из карточки с идентификатором
sourceCardID в карточку с идентификатором targetCardID с изменением ссылки на
задание targetTaskID. При этом контент файлов не перемещается между
карточками, для этого используйте метод
[Tessa.Cards.ComponentModel.ICardContentStrategy.MoveFiles].  
[MoveFilesAsync](M_Tessa_Cards_ComponentModel_ICardStoreStrategy_MoveFilesAsync.htm)|
Перемещает записи в секции по файлам из карточки с идентификатором
sourceCardID в карточку с идентификатором targetCardID. При этом контент
файлов не перемещается между карточками, для этого используйте метод
[Tessa.Cards.ComponentModel.ICardContentStrategy.MoveFiles].  
[StoreAsync](M_Tessa_Cards_ComponentModel_ICardStoreStrategy_StoreAsync.htm)|
Сохраняет карточку, данные её секций, файлы и задания.  
[TryGetCardTypeIDAsync](M_Tessa_Cards_ComponentModel_ICardStoreStrategy_TryGetCardTypeIDAsync.htm)|
Возвращает идентификатор типа карточки или null, если карточка с заданным
идентификатором уже существует.  
[TryGetTemporaryRolesAsync](M_Tessa_Cards_ComponentModel_ICardStoreStrategy_TryGetTemporaryRolesAsync.htm)|
Заполняет в карточке отсутствующую информацию по временным ролям, на которые
назначены сохраняемые задания, а именно имена этих ролей, а также по авторам
задания, а именно по идентификатору, имени и должности автора. Возвращает
список временных ролей, которые требуется заполнить и добавить в процессе
сохранения карточки, или null, если при формировании списка произошли ошибки и
выполнение следует прервать.  
[UpdateOriginalTaskInfoAsync](M_Tessa_Cards_ComponentModel_ICardStoreStrategy_UpdateOriginalTaskInfoAsync.htm)|
Заполняет в заданиях информацию по текущим ролям, на которые были назначены
задания, из базы данных, если это актуально для текущего сохранения (например,
если роль изменяется в процессе сохранения).  
[UpdateTaskPlannedAsync](M_Tessa_Cards_ComponentModel_ICardStoreStrategy_UpdateTaskPlannedAsync.htm)|
Заполняет в заданиях информацию о плановом завершении на основании срока,
указанного в задании.  
[UpdateTimeZoneTaskInfoAsync](M_Tessa_Cards_ComponentModel_ICardStoreStrategy_UpdateTimeZoneTaskInfoAsync.htm)|
Заполняет в заданиях информацию по временныс зонам.  
## __См. также
#### Ссылки
[ICardStoreStrategy - ](T_Tessa_Cards_ComponentModel_ICardStoreStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
