# IKrTokenProvider - интерфейс
Объект, обеспечивающий создание и валидацию токена безопасности для типового
решения.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess](N_Tessa_Extensions_Default_Server_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrTokenProvider
VB __Копировать
     Public Interface IKrTokenProvider
C++ __Копировать
     public interface class IKrTokenProvider
F# __Копировать
     type IKrTokenProvider = interface end
##  __Методы
[CreateToken(Card, Int64, ICollection<KrPermissionFlagDescriptor>,
IKrPermissionExtendedCardSettings,
Action<KrToken>)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_IKrTokenProvider_CreateToken_1.htm)|
Создаёт подписанный токен безопасности для заданной карточки с указанием прав
для процесса согласования.  
---|---  
[CreateToken(Guid, Int32, Int64, ICollection<KrPermissionFlagDescriptor>,
IKrPermissionExtendedCardSettings,
Action<KrToken>)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_IKrTokenProvider_CreateToken.htm)|
Создаёт подписанный токен безопасности для заданной информации по карточке с
указанием прав для процесса согласования.  
[ValidateTokenAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_IKrTokenProvider_ValidateTokenAsync.htm)|
Выполняет проверку валидности токена безопасности, что гарантирует его
неизменность с момента подписания. Возвращает признак того, что токен успешно
прошёл все проверки.  
## __Методы расширения
[CreateFullToken](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrTokenProviderExtensions_CreateFullToken_1.htm)|
Метод для создания токена прав доступа, содержащего все права и рассчитанные
расширенные настройки прав доступа.  
(Определяется
[KrTokenProviderExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrTokenProviderExtensions.htm))  
---|---  
[CreateFullToken](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrTokenProviderExtensions_CreateFullToken.htm)|
Метод для создания токена прав доступа, содержащего все права и рассчитанные
расширенные настройки прав доступа.  
(Определяется
[KrTokenProviderExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrTokenProviderExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess.htm)
