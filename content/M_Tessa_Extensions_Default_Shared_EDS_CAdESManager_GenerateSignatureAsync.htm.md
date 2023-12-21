# CAdESManager.GenerateSignatureAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.EDS](N_Tessa_Extensions_Default_Shared_EDS.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract ValueTask<byte[]> GenerateSignatureAsync(
    	byte[] certificate,
    	ISignatureFile file,
    	string digestOid,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public MustOverride Function GenerateSignatureAsync ( 
    	certificate As Byte(),
    	file As ISignatureFile,
    	digestOid As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Byte())
C++ __Копировать
     public:
    virtual ValueTask<array<unsigned char>^> GenerateSignatureAsync(
    	array<unsigned char>^ certificate, 
    	ISignatureFile^ file, 
    	String^ digestOid, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract GenerateSignatureAsync : 
            certificate : byte[] * 
            file : ISignatureFile * 
            digestOid : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<byte[]> 
#### Параметры
certificate [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
file [ISignatureFile](T_Tessa_Platform_EDS_ISignatureFile.htm)
digestOid [String](https://learn.microsoft.com/dotnet/api/system.string)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]>
#### Реализации
[IEDSManager.GenerateSignatureAsync(Byte[], ISignatureFile, String,
CancellationToken)](M_Tessa_Platform_EDS_IEDSManager_GenerateSignatureAsync.htm)  
##  __См. также
#### Ссылки
[CAdESManager - ](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm)
[Tessa.Extensions.Default.Shared.EDS - пространство
имён](N_Tessa_Extensions_Default_Shared_EDS.htm)
