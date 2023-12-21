# CardTask - свойства
##  __Свойства
[Action](P_Tessa_Cards_CardTask_Action.htm)|  Действие, выполняемое для
задания. По умолчанию имеет значение Create.  
---|---  
[AuthorID](P_Tessa_Cards_CardTask_AuthorID.htm)|  Идентификатор автора задания
или null, если задание не было создано и в качестве автора используется
текущий пользователь.  
[AuthorName](P_Tessa_Cards_CardTask_AuthorName.htm)|  Имя автора задания или
null, если задание не было создано и в качестве автора используется текущий
пользователь или если имя автора будет определено автоматически при
сохранении. Автоматическое определение возможно, если значение этого свойства
равно null. Внимание! Должность автора
[AuthorPosition](P_Tessa_Cards_CardTask_AuthorPosition.htm) автоматически
заполняется только в том случае, если имя указано как null.  
[AuthorPosition](P_Tessa_Cards_CardTask_AuthorPosition.htm)|  Должность автора
задания или null, если задание не было создано и в качестве автора
используется текущий пользователь или если должность автора будет определена
автоматически при сохранении. Автоматическое определение возможно, если
значение свойства [AuthorName](P_Tessa_Cards_CardTask_AuthorName.htm) равно
null.  
[CanPostpone](P_Tessa_Cards_CardTask_CanPostpone.htm)|  Получает или задаёт
признак того, что задание может быть отложено. Этот флаг не влияет на
сохранение задания.  
[CanPostponeEffective](P_Tessa_Cards_CardTask_CanPostponeEffective.htm)|
Возможность откладывания задания
[CanPostpone](P_Tessa_Cards_CardTask_CanPostpone.htm), полученная с учётом
признака
[CanPostponeExplicit](P_Tessa_Cards_CardTask_CanPostponeExplicit.htm).  
[CanPostponeExplicit](P_Tessa_Cards_CardTask_CanPostponeExplicit.htm)|
Признак того, что для задания требуется принудительно установить возможность
откладывания [CanPostpone](P_Tessa_Cards_CardTask_CanPostpone.htm).  
[Card](P_Tessa_Cards_CardTask_Card.htm)|  Карточка задания.  
[Digest](P_Tessa_Cards_CardTask_Digest.htm)|  Digest задания, или null, если
задание ещё не создано или Digest задания не указан. Digest содержит
произвольный текст, описывающий задание и выводимый пользователям. Значение
нельзя изменить после того, как задание было создано.  
[Dynamic](P_Tessa_Cards_CardInfoStorageObject_Dynamic.htm)|  Объект,
осуществляющий доступ к текущему объекту через позднее связывание свойств.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[DynamicInfo](P_Tessa_Cards_CardInfoStorageObject_DynamicInfo.htm)|  Объект,
осуществляющий доступ к дополнительной пользовательской информации по текущему
объекту через позднее связывание свойств.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[Flags](P_Tessa_Cards_CardTask_Flags.htm)|  Флаги задания.  
[GroupRowID](P_Tessa_Cards_CardTask_GroupRowID.htm)|  Идентификатор группы
истории заданий.  
[HistoryItemParentRowID](P_Tessa_Cards_CardTask_HistoryItemParentRowID.htm)|
Ссылка на родительскую запись в истории заданий, которая учитывается только
при автоматическом создании записи в истории заданий в процессе сохранения
карточки. При создании и загрузке карточки поле не заполняется и равно null.  
[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm)|  Дополнительная
пользовательская информация.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[InProgress](P_Tessa_Cards_CardTask_InProgress.htm)|  Дата взятия задания в
работу или null, если задание ещё не было взято в работу.  
[IsAuthor](P_Tessa_Cards_CardTask_IsAuthor.htm)|  Пользователь видит задание
как автор. Он входит в персональную роль автора задания как пользователь или
заместитель.  
[IsAuthorDeputy](P_Tessa_Cards_CardTask_IsAuthorDeputy.htm)|  Пользователь
видит задание как автор, т.к. является заместителем. Он входит в персональную
роль автора задания как пользователь или заместитель.  
[IsHidden](P_Tessa_Cards_CardTask_IsHidden.htm)|  Признак того, что задание не
следует показывать в UI несмотря на то, что оно присутствует в карточке.  
[IsHiddenFromAuthor](P_Tessa_Cards_CardTask_IsHiddenFromAuthor.htm)|  Получает
или задаёт признак того, что задание помечено как скрытое от автора. Этот флаг
влияет на сохранение задания.  
[IsLocked](P_Tessa_Cards_CardTask_IsLocked.htm)|  Задание не содержит
загруженных данных и доступно только для просмотра общей информации.  
[IsLockedEffective](P_Tessa_Cards_CardTask_IsLockedEffective.htm)|  Режим
просмотра [IsLocked](P_Tessa_Cards_CardTask_IsLocked.htm), полученный с учётом
признака [IsLockedExplicit](P_Tessa_Cards_CardTask_IsLockedExplicit.htm).  
[IsLockedExplicit](P_Tessa_Cards_CardTask_IsLockedExplicit.htm)|  Признак
того, что для задания требуется принудительно установить режим просмотра
[IsLocked](P_Tessa_Cards_CardTask_IsLocked.htm).  
[IsPerformer](P_Tessa_Cards_CardTask_IsPerformer.htm)|  Пользователь видит
задание как исполнитель. Либо он входит в роль, на которую назначено задание,
как пользователь или заместитель; либо он взял задание в работу, даже если уже
не входит в роль; либо он является заместителем пользователя, взявшего задание
в работу, в роли, на которую назначено задание.  
[IsPerformerDeputy](P_Tessa_Cards_CardTask_IsPerformerDeputy.htm)|
Пользователь видит задание как исполнитель, т.к. является заместителем. Либо
он входит в роль, на которую назначено задание, как заместитель; либо он
является заместителем пользователя, взявшего задание в работу, в роли, на
которую назначено задание.  
[IsPostponed](P_Tessa_Cards_CardTask_IsPostponed.htm)|  Задание отложено. Флаг
устанавливается при загрузке и не влияет на сохранение.  
[IsSystem](P_Tessa_Cards_CardTask_IsSystem.htm)|  Пользователь видит задание
как системный пользователь с особыми привилегиями.  
[OptionID](P_Tessa_Cards_CardTask_OptionID.htm)|  Идентификатор варианта
завершения задания, или null, если для задания ещё не был определён вариант
завершения.  
[OriginalRoleID](P_Tessa_Cards_CardTask_OriginalRoleID.htm)|  Идентификатор
текущей роли [RoleID](P_Tessa_Cards_CardTask_RoleID.htm), если роль изменяется
с флагом [UpdateRole](T_Tessa_Cards_CardTaskFlags.htm), или null, если роль не
изменяется или если значение ещё не заполнено платформой. Это свойство
используется платформой, не рекомендуется устанавливать его значение вручную.  
[OriginalRoleTypeID](P_Tessa_Cards_CardTask_OriginalRoleTypeID.htm)|
Идентификатор типа текущей роли
[RoleTypeID](P_Tessa_Cards_CardTask_RoleTypeID.htm), если роль изменяется с
флагом [UpdateRole](T_Tessa_Cards_CardTaskFlags.htm), или null, если роль не
изменяется или если значение ещё не заполнено платформой. Это свойство
используется платформой, не рекомендуется устанавливать его значение вручную.  
[ParentRowID](P_Tessa_Cards_CardTask_ParentRowID.htm)|  Ссылка на родительское
задание.  
[Planned](P_Tessa_Cards_CardTask_Planned.htm)|  Дата запланированного
завершения задания или null, если задание ещё не было создано.  
[PlannedQuants](P_Tessa_Cards_CardTask_PlannedQuants.htm)|  Количество квантов
календаря от времени на момент загрузки задания до времени его
запланированного завершения [Planned](P_Tessa_Cards_CardTask_Planned.htm) или
null, если задание ещё не было создано. Если возвращаемое количество квантов
отрицательное, то задание просрочено.  
[PlannedType](P_Tessa_Cards_CardTask_PlannedType.htm)|  Тип запаланированного
времени. В зависимости от указанного - трактует
[Planned](P_Tessa_Cards_CardTask_Planned.htm), как время исполнителя или
автора.  
[PostponeComment](P_Tessa_Cards_CardTask_PostponeComment.htm)|  Комментарий по
откладыванию задания или null, если задание не было отложено или пользователь
не задал комментария. Поле устанавливается пользователем при откладывании
задания.  
[Postponed](P_Tessa_Cards_CardTask_Postponed.htm)|  Дата и время, когда было
отложено задание, или null, если задание не было отложено. Поле
устанавливается системой при откладывании задания.  
[PostponedTo](P_Tessa_Cards_CardTask_PostponedTo.htm)|  Дата и время, до
которого было отложено задание, или null, если задание не было отложено. Поле
устанавливается пользователем при откладывании задания.  
[ProcessID](P_Tessa_Cards_CardTask_ProcessID.htm)|  Идентификатор бизнес-
процесса, к которому относится запись в истории заданий, которая будет
добавлена для задания, или null, если запись не относится к бизнес-процессу.
Свойство следует устанавливать перед изменением или завершением задания, для
которого будет добавлена запись в истории. Свойство не изменяется при
изменении записи в истории. По умолчанию значение равно null.  
[ProcessKind](P_Tessa_Cards_CardTask_ProcessKind.htm)|  Тип бизнес-процесса, к
которому относится запись в истории заданий, которая будет добавлена для
задания, или null, если запись не относится к бизнес-процессу или не содержит
информации по его типу. Свойство следует устанавливать перед изменением или
завершением задания, для которого будет добавлена запись в истории. Свойство
не изменяется при изменении записи в истории. По умолчанию значение равно
null.  
[ProcessName](P_Tessa_Cards_CardTask_ProcessName.htm)|  Отображаемое имя
бизнес-процесса, к которому относится запись в истории заданий, которая будет
добавлена для задания, или null, если запись не относится к бизнес-процессу.
Свойство следует устанавливать перед изменением или завершением задания, для
которого будет добавлена запись в истории. Свойство не изменяется при
изменении записи в истории. По умолчанию значение равно null.  
[Result](P_Tessa_Cards_CardTask_Result.htm)|  Результат завершения задания,
или null, если либо задание не завершается, либо результат устанавливается
серверными расширениями или не устанавливается вообще. Результат может быть
установлен не только при завершении задания, но и при создании записи в
истории заданий посредством указания флага
[CreateHistoryItem](T_Tessa_Cards_CardTaskFlags.htm).  
[RoleID](P_Tessa_Cards_CardTask_RoleID.htm)|  Идентификатор роли, на которую
назначено задание.  
[RoleName](P_Tessa_Cards_CardTask_RoleName.htm)|  Имя роли, на которую
назначено задание, или null, если задание ещё не было создано.  
[RoleTypeID](P_Tessa_Cards_CardTask_RoleTypeID.htm)|  Идентификатор типа
карточки для роли, на которую назначено задание, или Empty, если задание ещё
не было создано.  
[RowID](P_Tessa_Cards_CardTask_RowID.htm)|  Идентификатор задания.  
[SectionRows](P_Tessa_Cards_CardTask_SectionRows.htm)|  Пустые строки
коллекционных и древовидных секций, доступные по имени секции. Могут
использоваться для редактирования карточки задания.  
[Settings](P_Tessa_Cards_CardTask_Settings.htm)|  Настройки задания,
сериализуемые в JSON.  
[State](P_Tessa_Cards_CardTask_State.htm)|  Состояние строки с заданием.  
[StoredState](P_Tessa_Cards_CardTask_StoredState.htm)|  Начальное состояние
задания при загрузке или Created, если задание создаётся в первый раз.  
[TimeZoneID](P_Tessa_Cards_CardTask_TimeZoneID.htm)|  Идентификатор временной
зоны задания.  
[TimeZoneUtcOffsetMinutes](P_Tessa_Cards_CardTask_TimeZoneUtcOffsetMinutes.htm)|
Смещение временной зоны задания.  
[TypeCaption](P_Tessa_Cards_CardTask_TypeCaption.htm)|  Отображаемое имя типа
задания.  
[TypeID](P_Tessa_Cards_CardTask_TypeID.htm)|  Идентификатор типа задания.  
[TypeName](P_Tessa_Cards_CardTask_TypeName.htm)|  Имя типа задания.  
[UserID](P_Tessa_Cards_CardTask_UserID.htm)|  Идентификатор пользователя,
который взял задание в работу, или null, если задание ещё не было взято в
работу.  
[UserName](P_Tessa_Cards_CardTask_UserName.htm)|  Имя пользователя, который
взял задание в работу, или null, если задание ещё не было взято в работу.  
## __См. также
#### Ссылки
[CardTask - ](T_Tessa_Cards_CardTask.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
