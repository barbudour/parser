# CAdESManager.VerifySignatureAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.EDS](N_Tessa_Extensions_Default_Shared_EDS.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract ValueTask<(bool success, string errorText)> VerifySignatureAsync(
    	byte[] encodedSignature,
    	ISignatureFile file,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public MustOverride Function VerifySignatureAsync ( 
    	encodedSignature As Byte(),
    	file As ISignatureFile,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of (success As Boolean, errorText As String))
C++ __Копировать
     public:
    virtual ValueTask<ValueTuple<bool, String^>> VerifySignatureAsync(
    	array<unsigned char>^ encodedSignature, 
    	ISignatureFile^ file, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract VerifySignatureAsync : 
            encodedSignature : byte[] * 
            file : ISignatureFile * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ValueTuple<bool, string>> 
#### Параметры
encodedSignature [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
file [ISignatureFile](T_Tessa_Platform_EDS_ISignatureFile.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean),
[String](https://learn.microsoft.com/dotnet/api/system.string)>>
#### Реализации
[IEDSManager.VerifySignatureAsync(Byte[], ISignatureFile,
CancellationToken)](M_Tessa_Platform_EDS_IEDSManager_VerifySignatureAsync.htm)  
##  __См. также
#### Ссылки
[CAdESManager - ](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm)
[Tessa.Extensions.Default.Shared.EDS - пространство
имён](N_Tessa_Extensions_Default_Shared_EDS.htm)
