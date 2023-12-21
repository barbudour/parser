# IImpersonationContext - интерфейс
Контекст имперсонализации, содержащий информацию об учётной записи, от имени
которой выполняется код.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IImpersonationContext
VB __Копировать
     Public Interface IImpersonationContext
C++ __Копировать
     public interface class IImpersonationContext
F# __Копировать
     type IImpersonationContext = interface end
##  __Свойства
[AuthenticationType](P_Tessa_Platform_Runtime_IImpersonationContext_AuthenticationType.htm)|
Тип аутентификации, который был использован для идентификации пользователя.  
---|---  
[Identity](P_Tessa_Platform_Runtime_IImpersonationContext_Identity.htm)|
Объект, специфичный для платформы (операционной системы), и соответствующий
учётной записи пользователя.  
[IsAnonymous](P_Tessa_Platform_Runtime_IImpersonationContext_IsAnonymous.htm)|
Признак того, что аккаунт пользователя был определён системой как анонимный.  
[IsAuthenticated](P_Tessa_Platform_Runtime_IImpersonationContext_IsAuthenticated.htm)|
Признак того, что аутентификация была выполнена.  
[IsGuest](P_Tessa_Platform_Runtime_IImpersonationContext_IsGuest.htm)| Признак
того, что аккаунт пользователя был определён системой как гостевой.  
[IsSystem](P_Tessa_Platform_Runtime_IImpersonationContext_IsSystem.htm)|
Признак того, что аккаунт пользователя был определён системой как системный.  
[Name](P_Tessa_Platform_Runtime_IImpersonationContext_Name.htm)| Имя учётной
записи пользователя, под которой был выполнен вход.  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
