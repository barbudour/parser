# EdsService - класс
##  __Definition
 **Пространство имён:** [Tessa.Host.EDS](N_Tessa_Host_EDS.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class EdsService : IEdsService, IAsyncDisposable, 
    	IDisposable
VB __Копировать
     Public Class EdsService
    	Implements IEdsService, IAsyncDisposable, IDisposable
C++ __Копировать
     public ref class EdsService : IEdsService, 
    	IAsyncDisposable, IDisposable
F# __Копировать
     type EdsService = 
        class
            interface IEdsService
            interface IAsyncDisposable
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ EdsService
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IEdsService](T_Tessa_Host_EDS_IEdsService.htm)
##  __Конструкторы
[EdsService](M_Tessa_Host_EDS_EdsService__ctor.htm)| Инициализирует новый
экземпляр класса EdsService  
---|---  
##  __Методы
[Dispose](M_Tessa_Host_EDS_EdsService_Dispose.htm)| Освобождает ресурсы,
занимаемые объектом.  
---|---  
[DisposeAsync](M_Tessa_Host_EDS_EdsService_DisposeAsync.htm)| Освобождает
ресурсы, занимаемые объектом.  
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
[GenerateSignatureAsync](M_Tessa_Host_EDS_EdsService_GenerateSignatureAsync.htm)|
Подписывает указанный файл заданным сертификатом и возвращает ЭП.
ВАЖНО: ЭП возвращается как объект
[SignedCms](https://learn.microsoft.com/dotnet/api/system.security.cryptography.pkcs.signedcms),
тогда как метод [GenerateSignatureAsync(Byte[], ISignatureFile, String,
CancellationToken)](M_Tessa_Platform_EDS_IEDSManager_GenerateSignatureAsync.htm)
должен вернуть signerInfo.GetSignature() для первого объекта из
signedCms.SignerInfos[0]. Поэтому эта обработка должна быть сделана в
реализации интерфейса [IEDSManager](T_Tessa_Platform_EDS_IEDSManager.htm),
которая делегирует вызовы в [IEdsService](T_Tessa_Host_EDS_IEdsService.htm)
для потенциального выполнения в другом процессе, а именно: var signedCms = new
SignedCms(); signedCms.Decode(encodedSignature); return
signedCms.SignerInfos[0].GetSignature();.  
[GenerateSignatureCore](M_Tessa_Host_EDS_EdsService_GenerateSignatureCore.htm)|  
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
[VerifySignatureAsync](M_Tessa_Host_EDS_EdsService_VerifySignatureAsync.htm)|
Выполняет проверку ЭП для содержимого файла. Возвращает признак success того,
что проверка прошла успешно. Если возвращаемое значение sucess равно false, то
в значении errorText указано сообщение об ошибке.  
[VerifySignatureCore](M_Tessa_Host_EDS_EdsService_VerifySignatureCore.htm)|  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
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
[Tessa.Host.EDS - пространство имён](N_Tessa_Host_EDS.htm)
