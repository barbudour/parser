# SignatureProviderNames - класс
Имена объектов [ISignatureProvider](T_Tessa_Platform_ISignatureProvider.htm),
которые регистрируются в Unity.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class SignatureProviderNames
VB __Копировать
     Public NotInheritable Class SignatureProviderNames
C++ __Копировать
     public ref class SignatureProviderNames abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type SignatureProviderNames = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SignatureProviderNames
##  __Поля
[AdSync](F_Tessa_Platform_SignatureProviderNames_AdSync.htm)|  Объект,
используемый для получения хеша AD / LDAP объекта. Реализация также доступна
через статическое свойство
[AdSync](P_Tessa_Platform_HashSignatureProvider_AdSync.htm).  
---|---  
[Files](F_Tessa_Platform_SignatureProviderNames_Files.htm)|  Объект,
используемый для расчёта подписи файлов. Зависимость доступна на клиенте (в
качестве зависимости по умолчанию), а также на сервере (как именованная
зависимость). Т.е. вызов unityContainer.Resolve<ISessionProvider>() вернёт
этот объект на клиенте. Реализация также доступна через статическое свойство
[Files](P_Tessa_Platform_HashSignatureProvider_Files.htm). На клиенте подпись
проверяется  
[License](F_Tessa_Platform_SignatureProviderNames_License.htm)|  Объект,
используемый для проверки подписи в лицензии.  
[Operations](F_Tessa_Platform_SignatureProviderNames_Operations.htm)|  Объект,
используемый при вычислении хеша для запроса
[RequestHash](P_Tessa_Platform_Operations_IOperation_RequestHash.htm) в
операциях
[IOperationRepository](T_Tessa_Platform_Operations_IOperationRepository.htm).
Зависимость доступна и на клиенте, и на сервере как именованная зависимость.
Реализация также доступна через статическое свойство
[Operations](P_Tessa_Platform_HashSignatureProvider_Operations.htm).  
[Session](F_Tessa_Platform_SignatureProviderNames_Session.htm)|  Объект,
используемый при подписании токена сессии
[ISessionToken](T_Tessa_Platform_Runtime_ISessionToken.htm). Зависимость
доступна только на сервере в качестве зависимости по умолчанию. Т.е. вызов
unityContainer.Resolve<ISessionProvider>() вернёт этот объект на сервере.  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
