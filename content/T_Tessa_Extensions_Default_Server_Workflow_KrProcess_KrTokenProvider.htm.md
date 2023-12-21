# KrTokenProvider - класс
Объект, обеспечивающий создание и валидацию токена безопасности для типового
решения.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess](N_Tessa_Extensions_Default_Server_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class KrTokenProvider : IKrTokenProvider
VB __Копировать
     Public Class KrTokenProvider
    	Implements IKrTokenProvider
C++ __Копировать
     public ref class KrTokenProvider : IKrTokenProvider
F# __Копировать
     type KrTokenProvider = 
        class
            interface IKrTokenProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrTokenProvider
Implements
    [IKrTokenProvider](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_IKrTokenProvider.htm)
##  __Заметки
Наследники класса могут переопределить методы и изменить свойства, в т.ч. срок
жизни выписанного токена
[TokenExpirationTimeSpan](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrTokenProvider_TokenExpirationTimeSpan.htm).
Зарегистрируйте наследник по интерфейсу
[IKrTokenProvider](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_IKrTokenProvider.htm),
указав в атрибуте [Registrator(Order = 1)], чтобы переопределить стандартную
регистрацию.
## __Конструкторы
[KrTokenProvider](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrTokenProvider__ctor.htm)|
Инициализирует новый экземпляр класса KrTokenProvider  
---|---  
##  __Свойства
[SignatureProvider](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrTokenProvider_SignatureProvider.htm)|  
---|---  
[TokenExpirationTimeSpan](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrTokenProvider_TokenExpirationTimeSpan.htm)|
Срок жизни выписанного токена при условии, что он не будет пересчитываться при
изменении версии карточки и расширение на права доступа не укажет, что токен
требуется пересчитать.  
## __Методы
[CreateToken(Card, Int64, ICollection<KrPermissionFlagDescriptor>,
IKrPermissionExtendedCardSettings,
Action<KrToken>)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrTokenProvider_CreateToken_1.htm)|
Создаёт подписанный токен безопасности для заданной карточки с указанием прав
для процесса согласования.  
---|---  
[CreateToken(Guid, Int32, Int64, ICollection<KrPermissionFlagDescriptor>,
IKrPermissionExtendedCardSettings,
Action<KrToken>)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrTokenProvider_CreateToken.htm)|
Создаёт подписанный токен безопасности для заданной информации по карточке с
указанием прав для процесса согласования.  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ValidateTokenAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrTokenProvider_ValidateTokenAsync.htm)|
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
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess.htm)
