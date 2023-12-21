# KrSettings - свойства
##  __Свойства
[ChildResolutionColumnCommentMaxLength](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_ChildResolutionColumnCommentMaxLength.htm)|
Максимальная длина для сокращённого комментария, выводимого в колонке таблицы
с дочерними резолюциями. Размер строки подобран таким образом, чтобы
комментарий помещался на одной строке с фразой "назначено на роль Исполнители
задания". По умолчанию значение равно 28.  
---|---  
[ChildResolutionColumnStateMaxLength](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_ChildResolutionColumnStateMaxLength.htm)|
Максимальная длина для информации о задании, выводимого в колонке таблицы с
дочерними резолюциями. По умолчанию значение равно 32.  
[CloseCardWhenCompletedEvents](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_CloseCardWhenCompletedEvents.htm)|
События, когда вкладка с карточкой должна быть автоматически закрыта. По
умолчанию значение равно None, т.е. автоматическое закрытие вкладки отключено
для всех событий.  
[CreateBasedOnTypes](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_CreateBasedOnTypes.htm)|
Типы карточек, для которых доступна плитка "Создать на основании".  
[DisableConfirmationEvents](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_DisableConfirmationEvents.htm)|
Отключает подтверждения в виде диалоговых окон, отображаемых для некоторых
действий в типовом решении, таких как запуск процесса согласования и
регистрация документа. По умолчанию значение равно None, т.е. подтверждения
включены для всех событий.  
[GetMultiplePerformersDefaults](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_GetMultiplePerformersDefaults.htm)|
Функция, принимающая объект WfResolutionTaskInfo, описывающий задание, и
возвращающая режим по умолчанию для флажков, которые устанавливаются в задаче
при выборе нескольких исполнителей. Режим по умолчанию определяет лишь
начальное состояние флажков, пользователь может его изменить.  
[NotificationCheckInterval](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_NotificationCheckInterval.htm)|
Интервал проверки на новые задания.  
[NotificationDuration](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_NotificationDuration.htm)|
Время отображения уведомлений по заданиям.  
[NotificationIntervalToGetTasksAfterInitialization](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_NotificationIntervalToGetTasksAfterInitialization.htm)|
При первом запуске (после старта приложения) загружаем задания за последний
час.  
[NotificationMaxTasksToDisplay](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_NotificationMaxTasksToDisplay.htm)|
Максимальное количество новых заданий, которое отображается в отдельных окнах
уведомлений. Задания отображаются в порядке сортировки
[NotificationSortingColumnDirection](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_NotificationSortingColumnDirection.htm)
по колонке
[NotificationSortingColumnAlias](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_NotificationSortingColumnAlias.htm).
В настройках по умолчанию отображается первые несколько новых заданий. Полный
список заданий пользователь сможет посмотреть, если перейдёт в представление
[NotificationViewAlias](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_NotificationViewAlias.htm)
при клике по уведомлению с информацией по количеству заданий.  
[NotificationNodeToOpenMyTasksID](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_NotificationNodeToOpenMyTasksID.htm)|
Идентификатор узла "Мои задания" в дереве рабочего места
[NotificationWorkplaceToOpenMyTasksID](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_NotificationWorkplaceToOpenMyTasksID.htm).  
[NotificationPageLimit](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_NotificationPageLimit.htm)|
Максимальное количество записей, загружаемых по умолчанию, если в "Моих
заданиях" доступен пейджинг. По умолчанию значение 10.  
[NotificationSortingColumnAlias](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_NotificationSortingColumnAlias.htm)|
Колонка для сортировки по умолчанию в представлении
[NotificationViewAlias](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_NotificationViewAlias.htm).
В колонке должно быть задано выражение SortBy, иначе сортировка будет по
колонке по умолчанию.  
[NotificationSortingColumnDirection](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_NotificationSortingColumnDirection.htm)|
Направление сортировки по умолчанию для колонки
[NotificationSortingColumnAlias](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_NotificationSortingColumnAlias.htm).  
[NotificationViewAlias](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_NotificationViewAlias.htm)|
Представление, которое возвращает список заданий.  
[NotificationWorkplaceToOpenMyTasksID](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_NotificationWorkplaceToOpenMyTasksID.htm)|
Идентификатор рабочего места "Пользователь".  
[ProtocolTaskDefaultDuration](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_ProtocolTaskDefaultDuration.htm)|
Планируемая длительность по умолчанию в днях по бизнес-календарю для заданий,
высылаемых по решениям протокола, когда для решений не было явно заданного
срока.  
[ResolutionControlDuration](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_ResolutionControlDuration.htm)|
Планируемая длительность по умолчанию в днях по бизнес-календарю для задания
контроля исполнения резолюции. По умолчанию значение равно 3.  
[ResolutionProjectDuration](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_ResolutionProjectDuration.htm)|
Планируемая длительность по умолчанию в днях по бизнес-календарю для задания
проекта резолюции. Указано на один день дольше, чем количество дней по
умолчанию, заполненное в поле "длительность", чтобы дочерняя резолюция в
течение первого дня создавалась бы с запланированной датой, которая
заканчивается раньше, чем у проекта резолюции. По умолчанию значение равно 3.  
[SafeChildResolutionTimeLimit](P_Tessa_Extensions_Default_Shared_Settings_KrSettings_SafeChildResolutionTimeLimit.htm)|
Количество дней, на которые время завершения дочерней резолюции может
превышать время завершения родительской, если в настройках типового решения
включено ограничение на дату дочерней резолюции. По умолчанию значение равно
1.0.  
## __См. также
#### Ссылки
[KrSettings - ](T_Tessa_Extensions_Default_Shared_Settings_KrSettings.htm)
[Tessa.Extensions.Default.Shared.Settings - пространство
имён](N_Tessa_Extensions_Default_Shared_Settings.htm)
