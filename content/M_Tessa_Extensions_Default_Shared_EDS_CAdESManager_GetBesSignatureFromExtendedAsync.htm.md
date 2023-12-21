# CAdESManager.GetBesSignatureFromExtendedAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.EDS](N_Tessa_Extensions_Default_Shared_EDS.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<byte[]> GetBesSignatureFromExtendedAsync(
    	byte[] signature,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetBesSignatureFromExtendedAsync ( 
    	signature As Byte(),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Byte())
C++ __Копировать
     public:
    virtual Task<array<unsigned char>^>^ GetBesSignatureFromExtendedAsync(
    	array<unsigned char>^ signature, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetBesSignatureFromExtendedAsync : 
            signature : byte[] * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<byte[]> 
    override GetBesSignatureFromExtendedAsync : 
            signature : byte[] * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<byte[]> 
#### Параметры
signature [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]>
#### Реализации
[ICAdESManager.GetBesSignatureFromExtendedAsync(Byte[],
CancellationToken)](M_Tessa_Platform_EDS_ICAdESManager_GetBesSignatureFromExtendedAsync.htm)  
##  __См. также
#### Ссылки
[CAdESManager - ](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm)
[Tessa.Extensions.Default.Shared.EDS - пространство
имён](N_Tessa_Extensions_Default_Shared_EDS.htm)
