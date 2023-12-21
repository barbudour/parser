# INotificationSendContext - интерфейс
Контекст отправки уведомления через
[INotificationManager](T_Tessa_Notices_INotificationManager.htm).
## __Definition
 **Пространство имён:** [Tessa.Notices](N_Tessa_Notices.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface INotificationSendContext
VB __Копировать
     Public Interface INotificationSendContext
C++ __Копировать
     public interface class INotificationSendContext
F# __Копировать
     type INotificationSendContext = interface end
##  __Свойства
[DisableSubscribers](P_Tessa_Notices_INotificationSendContext_DisableSubscribers.htm)|
Флаг определяет, нужно ли исключить из списка получателей подписчиков на
данный тип уведомления для данной карточки.  
---|---  
[ExcludeDeputies](P_Tessa_Notices_INotificationSendContext_ExcludeDeputies.htm)|
Флаг определяет, нужно ли исключить из списка сотрудников заместителей.  
[GetCardFuncAsync](P_Tessa_Notices_INotificationSendContext_GetCardFuncAsync.htm)|
Функция для получения объекта карточки из кеша. Может иметь значение null.  
[IgnoreUserSessions](P_Tessa_Notices_INotificationSendContext_IgnoreUserSessions.htm)|
Флаг определяет, нужно ли игнорировать сессии пользователей при формировании
текста писем. Игнорирование сессии ускоряет скорость отправки писем, однако в
данном режиме не работают плейсхолдеры, которые опираются на сессию
получателя.  
[Info](P_Tessa_Notices_INotificationSendContext_Info.htm)|  Дополнительная
информация, которая передается в info методов замены плейсхолдеров.  
[MainCardID](P_Tessa_Notices_INotificationSendContext_MainCardID.htm)|
Идентификатор основной карточки.  
[ModifyEmailActionAsync](P_Tessa_Notices_INotificationSendContext_ModifyEmailActionAsync.htm)|
Действие модификации шаблона сообщения.  
## __См. также
#### Ссылки
[Tessa.Notices - пространство имён](N_Tessa_Notices.htm)
