# FileExtensionHelper.FilterActionAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Files](N_Tessa_Extensions_Platform_Client_Files.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static Func<X509Certificate2Collection, CancellationToken, Task> FilterActionAsync(
    	ICardCache cardCache
    )
VB __Копировать
     Public Shared Function FilterActionAsync ( 
    	cardCache As ICardCache
    ) As Func(Of X509Certificate2Collection, CancellationToken, Task)
C++ __Копировать
     public:
    static Func<X509Certificate2Collection^, CancellationToken, Task^>^ FilterActionAsync(
    	ICardCache^ cardCache
    )
F# __Копировать
     static member FilterActionAsync : 
            cardCache : ICardCache -> Func<X509Certificate2Collection, CancellationToken, Task> 
#### Параметры
cardCache [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)
#### Возвращаемое значение
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[X509Certificate2Collection](https://learn.microsoft.com/dotnet/api/system.security.cryptography.x509certificates.x509certificate2collection),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)>
##  __См. также
#### Ссылки
[FileExtensionHelper -
](T_Tessa_Extensions_Platform_Client_Files_FileExtensionHelper.htm)
[Tessa.Extensions.Platform.Client.Files - пространство
имён](N_Tessa_Extensions_Platform_Client_Files.htm)
