# CAdESManager.GetSignatureBytesFromFileAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.EDS](N_Tessa_Extensions_Default_Shared_EDS.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual ValueTask<byte[]> GetSignatureBytesFromFileAsync(
    	string filePath,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overridable Function GetSignatureBytesFromFileAsync ( 
    	filePath As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Byte())
C++ __Копировать
     public:
    virtual ValueTask<array<unsigned char>^> GetSignatureBytesFromFileAsync(
    	String^ filePath, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetSignatureBytesFromFileAsync : 
            filePath : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<byte[]> 
    override GetSignatureBytesFromFileAsync : 
            filePath : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<byte[]> 
#### Параметры
filePath [String](https://learn.microsoft.com/dotnet/api/system.string)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]>
#### Реализации
[IEDSManager.GetSignatureBytesFromFileAsync(String,
CancellationToken)](M_Tessa_Platform_EDS_IEDSManager_GetSignatureBytesFromFileAsync.htm)  
##  __См. также
#### Ссылки
[CAdESManager - ](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm)
[Tessa.Extensions.Default.Shared.EDS - пространство
имён](N_Tessa_Extensions_Default_Shared_EDS.htm)
