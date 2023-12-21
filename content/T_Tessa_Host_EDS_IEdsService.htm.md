# IEdsService - интерфейс
Сервис для взаимодействия с приложениями, осуществляющими подписание ЭП и
проверку подписи.
## __Definition
 **Пространство имён:** [Tessa.Host.EDS](N_Tessa_Host_EDS.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IEdsService : IAsyncDisposable, 
    	IDisposable
VB __Копировать
     Public Interface IEdsService
    	Inherits IAsyncDisposable, IDisposable
C++ __Копировать
     public interface class IEdsService : IAsyncDisposable, 
    	IDisposable
F# __Копировать
     type IEdsService = 
        interface
            interface IAsyncDisposable
            interface IDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Методы
[Dispose](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose)| Performs application-defined tasks associated with
freeing, releasing, or resetting unmanaged resources.  
(Унаследован от
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable))  
---|---  
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
[GenerateSignatureAsync](M_Tessa_Host_EDS_IEdsService_GenerateSignatureAsync.htm)|
Подписывает указанный файл заданным сертификатом и возвращает ЭП.
ВАЖНО: ЭП возвращается как объект
[SignedCms](https://learn.microsoft.com/dotnet/api/system.security.cryptography.pkcs.signedcms),
тогда как метод [GenerateSignatureAsync(Byte[], ISignatureFile, String,
CancellationToken)](M_Tessa_Platform_EDS_IEDSManager_GenerateSignatureAsync.htm)
должен вернуть signerInfo.GetSignature() для первого объекта из
signedCms.SignerInfos[0]. Поэтому эта обработка должна быть сделана в
реализации интерфейса [IEDSManager](T_Tessa_Platform_EDS_IEDSManager.htm),
которая делегирует вызовы в IEdsService для потенциального выполнения в другом
процессе, а именно: var signedCms = new SignedCms();
signedCms.Decode(encodedSignature); return
signedCms.SignerInfos[0].GetSignature();.  
[VerifySignatureAsync](M_Tessa_Host_EDS_IEdsService_VerifySignatureAsync.htm)|
Выполняет проверку ЭП для содержимого файла. Возвращает признак success того,
что проверка прошла успешно. Если возвращаемое значение sucess равно false, то
в значении errorText указано сообщение об ошибке.  
## __См. также
#### Ссылки
[Tessa.Host.EDS - пространство имён](N_Tessa_Host_EDS.htm)
