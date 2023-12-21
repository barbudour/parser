# FakeSignatureProvider - класс
Реализация [ISignatureProvider](T_Tessa_Platform_ISignatureProvider.htm), не
выполняющая действий по подписыванию и проверке подписи. Метод
[Sign(Byte[])](M_Tessa_Platform_FakeSignatureProvider_Sign.htm) всегда
возвращает заданные данные без изменений, а метод [Verify(Byte[],
Byte[])](M_Tessa_Platform_FakeSignatureProvider_Verify.htm) всегда возвращает
true.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FakeSignatureProvider : ISignatureProvider
VB __Копировать
     Public NotInheritable Class FakeSignatureProvider
    	Implements ISignatureProvider
C++ __Копировать
     public ref class FakeSignatureProvider sealed : ISignatureProvider
F# __Копировать
     [<SealedAttribute>]
    type FakeSignatureProvider = 
        class
            interface ISignatureProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FakeSignatureProvider
Implements
    [ISignatureProvider](T_Tessa_Platform_ISignatureProvider.htm)
##  __Конструкторы
[FakeSignatureProvider](M_Tessa_Platform_FakeSignatureProvider__ctor.htm)|
Инициализирует новый экземпляр класса FakeSignatureProvider  
---|---  
##  __Свойства
[Instance](P_Tessa_Platform_FakeSignatureProvider_Instance.htm)| Экземпляр
класса.  
---|---  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
[Sign](M_Tessa_Platform_FakeSignatureProvider_Sign.htm)|  Возвращает
электронную цифровую подпись для заданных бинарных данных лицензии.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Verify](M_Tessa_Platform_FakeSignatureProvider_Verify.htm)|  Проверяет
валидность электронной цифровой подписи для заданных бинарных данных лицензии.  
## __Методы расширения
[GenerateSignature](M_Tessa_Platform_Runtime_RuntimeExtensions_GenerateSignature.htm)|
Создаёт подпись для заданных свойств, связанных с сессией.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
---|---  
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
[ValidateType](M_Tessa_Platform_Licensing_LicensingExtensions_ValidateType.htm)|
Проверяет, что тип объекта является допустимым. Это гарантирует, что объект не
был нигде подменён злоумышленником.  
(Определяется
[LicensingExtensions](T_Tessa_Platform_Licensing_LicensingExtensions.htm))  
[VerifySignature](M_Tessa_Platform_Runtime_RuntimeExtensions_VerifySignature_1.htm)|
Выполняет проверку подписи для заданного токена
[ISessionToken](T_Tessa_Platform_Runtime_ISessionToken.htm) и возвращает
признак того, что подпись корректна.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
[VerifySignature](M_Tessa_Platform_Runtime_RuntimeExtensions_VerifySignature.htm)|
Выполняет проверку подписи для заданных свойств, связанных с сессией, и
возвращает признак того, что подпись корректна.  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
