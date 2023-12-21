# INotificationContext.CardDigest - свойство
Digest карточки или null, если Digest недоступен. Локализация должна быть
выполнена индивидуально для каждого уведомления на языке пользователя, который
получит уведомление. Локализацию требуется выполнять методом
[Format(String)](M_Tessa_Localization_LocalizationManager_Format.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Notices](N_Tessa_Extensions_Default_Shared_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     string CardDigest { get; }
VB __Копировать
     ReadOnly Property CardDigest As String
    	Get
C++ __Копировать
    property String^ CardDigest {
    	String^ get ();
    }
F# __Копировать
     abstract CardDigest : string with get
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[INotificationContext -
](T_Tessa_Extensions_Default_Shared_Notices_INotificationContext.htm)
[Tessa.Extensions.Default.Shared.Notices - пространство
имён](N_Tessa_Extensions_Default_Shared_Notices.htm)
