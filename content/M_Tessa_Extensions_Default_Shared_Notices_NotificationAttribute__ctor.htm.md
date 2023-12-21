# NotificationAttribute - конструктор
Создаёт атрибут с указанием его свойств.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Notices](N_Tessa_Extensions_Default_Shared_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public NotificationAttribute(
    	string key
    )
VB __Копировать
     Public Sub New ( 
    	key As String
    )
C++ __Копировать
     public:
    NotificationAttribute(
    	String^ key
    )
F# __Копировать
     new : 
            key : string -> NotificationAttribute
#### Параметры
key [String](https://learn.microsoft.com/dotnet/api/system.string)
     Ключ, по которому регистрируются обработчики [INotificationSender](T_Tessa_Extensions_Default_Shared_Notices_INotificationSender.htm) и который определяет имя вложенной секции для сериализации сообщений. Ключ должен быть уникален для каждого типа уведомлений. 
## __См. также
#### Ссылки
[NotificationAttribute -
](T_Tessa_Extensions_Default_Shared_Notices_NotificationAttribute.htm)
[Tessa.Extensions.Default.Shared.Notices - пространство
имён](N_Tessa_Extensions_Default_Shared_Notices.htm)
