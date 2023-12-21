# Tessa.Notices.Sources - пространство имён
## __Классы
[AggregateNotificationRecipientsSource](T_Tessa_Notices_Sources_AggregateNotificationRecipientsSource.htm)|
Реализация
[INotificationRecipientsSource](T_Tessa_Notices_Sources_INotificationRecipientsSource.htm),
которая обрабатывает
[AggregateNotificationRecipientsSourceParameter](T_Tessa_Notices_Parameters_AggregateNotificationRecipientsSourceParameter.htm).
При вычислении получателей по нескольким параметрам объединяет результат по
паре значений [UserID](P_Tessa_Notices_NotificationRecipient_UserID.htm) и
[Email](P_Tessa_Notices_NotificationRecipient_Email.htm). Параметр
[IsOptional](P_Tessa_Notices_NotificationRecipient_IsOptional.htm) берётся как
false, если для одного получателя при расчёте по различным параметрам есть
разные значения этого параметра. Остальные настройки у объединённого списка
получателей берутся в приоритете из параметра, что был в списке раньше.  
---|---  
[AliasNotificationEmailSource](T_Tessa_Notices_Sources_AliasNotificationEmailSource.htm)|
Реализация
[INotificationEmailSource](T_Tessa_Notices_Sources_INotificationEmailSource.htm),
которая возвращает шаблон уведомления по алиасу карточки уведомления.
Обрабатывает параметр с типом
[AliasNotificationEmailSourceParameter](T_Tessa_Notices_Parameters_AliasNotificationEmailSourceParameter.htm).  
[EmailsNotificationRecipientsSource](T_Tessa_Notices_Sources_EmailsNotificationRecipientsSource.htm)|
Реализация
[INotificationRecipientsSource](T_Tessa_Notices_Sources_INotificationRecipientsSource.htm),
которая получает список получателей как список явно заданных email-ов с
указанием идентификатора пользователя, настройки которого исопльзуются для
формирования письма. Обрабатывает тип параметров
[EmailsNotificationRecipientsSourceParameter](T_Tessa_Notices_Parameters_EmailsNotificationRecipientsSourceParameter.htm).  
[NotificationEmailSource](T_Tessa_Notices_Sources_NotificationEmailSource.htm)|
Реализация
[INotificationEmailSource](T_Tessa_Notices_Sources_INotificationEmailSource.htm),
которая возвращает шаблон уведомления по идентификатору карточки уведомления.
Базовая версия обрабатывает параметр с типом
[IDNotificationEmailSourceParameter](T_Tessa_Notices_Parameters_IDNotificationEmailSourceParameter.htm).  
[NotificationEmailSourceResolver](T_Tessa_Notices_Sources_NotificationEmailSourceResolver.htm)|
Объект, используемый для запросов типов сервисов по ключу, например, по имени.  
[NotificationRecipientsSource](T_Tessa_Notices_Sources_NotificationRecipientsSource.htm)|
Реализация
[INotificationRecipientsSource](T_Tessa_Notices_Sources_INotificationRecipientsSource.htm),
которая получает список получателей по списку идентификаторов ролей.
Обрабатывает тип параметров
[IDNotificationRecipientsSourceParameter](T_Tessa_Notices_Parameters_IDNotificationRecipientsSourceParameter.htm).
Учитывает настройки заместителей в
[INotificationSendContext](T_Tessa_Notices_INotificationSendContext.htm).  
[NotificationRecipientsSourceResolver](T_Tessa_Notices_Sources_NotificationRecipientsSourceResolver.htm)|
Объект, используемый для запросов типов сервисов по ключу, например, по имени.  
[ObviousNotificationEmailSource](T_Tessa_Notices_Sources_ObviousNotificationEmailSource.htm)|
Реализация
[INotificationEmailSource](T_Tessa_Notices_Sources_INotificationEmailSource.htm),
которая обрабатывает явно
[ObviousNotificationEmailSourceParameter](T_Tessa_Notices_Parameters_ObviousNotificationEmailSourceParameter.htm).  
[ObviousNotificationRecipientsSource](T_Tessa_Notices_Sources_ObviousNotificationRecipientsSource.htm)|
Реализация
[INotificationRecipientsSource](T_Tessa_Notices_Sources_INotificationRecipientsSource.htm),
которая обрабатывает явно
[ObviousNotificationRecipientsSourceParameter](T_Tessa_Notices_Parameters_ObviousNotificationRecipientsSourceParameter.htm).  
[RoleNameNotificationRecipientsSource](T_Tessa_Notices_Sources_RoleNameNotificationRecipientsSource.htm)|
Реализация
[INotificationRecipientsSource](T_Tessa_Notices_Sources_INotificationRecipientsSource.htm),
которая получает список получателей по списку имен ролей. Обрабатывает тип
параметров
[RoleNameNotificationRecipientsSourceParameter](T_Tessa_Notices_Parameters_RoleNameNotificationRecipientsSourceParameter.htm).
Учитывает настройки заместителей в
[INotificationSendContext](T_Tessa_Notices_INotificationSendContext.htm).  
## __Интерфейсы
[INotificationEmailSource](T_Tessa_Notices_Sources_INotificationEmailSource.htm)|
Источник уведомления для отправки.  
---|---  
[INotificationEmailSourceResolver](T_Tessa_Notices_Sources_INotificationEmailSourceResolver.htm)|
Объект для получения источника шаблонов уведомлений по параметру уведомления.  
[INotificationRecipientsSource](T_Tessa_Notices_Sources_INotificationRecipientsSource.htm)|
Источник получателей для уведомления.  
[INotificationRecipientsSourceResolver](T_Tessa_Notices_Sources_INotificationRecipientsSourceResolver.htm)|
Объект для получения источника получателей уведомления по параметру.
