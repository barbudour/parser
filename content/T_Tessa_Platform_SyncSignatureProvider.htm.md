# SyncSignatureProvider - класс
Объект, предоставляющий криптографические средства для подписания и проверки
подписи синхронным методом
[HMACSHA256](https://learn.microsoft.com/dotnet/api/system.security.cryptography.hmacsha256)
с указанием ключа подписи.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SyncSignatureProvider : HashSignatureProvider
VB __Копировать
     Public NotInheritable Class SyncSignatureProvider
    	Inherits HashSignatureProvider
C++ __Копировать
     public ref class SyncSignatureProvider sealed : public HashSignatureProvider
F# __Копировать
     [<SealedAttribute>]
    type SyncSignatureProvider = 
        class
            inherit HashSignatureProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[HashSignatureProvider](T_Tessa_Platform_HashSignatureProvider.htm) __ SyncSignatureProvider
##  __Конструкторы
[SyncSignatureProvider](M_Tessa_Platform_SyncSignatureProvider__ctor.htm)|
Создаёт экземпляр класса с указанием ключа, используемого для подписи и для
проверки подписи.  
---|---  
## __Методы
[CreateAlgorithm](M_Tessa_Platform_SyncSignatureProvider_CreateAlgorithm.htm)|
Создаёт алгоритм вычисления хеша.  
(Переопределяет
[HashSignatureProvider.CreateAlgorithm()](M_Tessa_Platform_HashSignatureProvider_CreateAlgorithm.htm))  
---|---  
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
[Sign](M_Tessa_Platform_HashSignatureProvider_Sign.htm)|  Возвращает
электронную цифровую подпись для заданных бинарных данных лицензии.  
(Унаследован от
[HashSignatureProvider](T_Tessa_Platform_HashSignatureProvider.htm))  
[SignCore](M_Tessa_Platform_HashSignatureProvider_SignCore.htm)|  Возвращает
электронную цифровую подпись для заданных бинарных данных лицензии.  
(Унаследован от
[HashSignatureProvider](T_Tessa_Platform_HashSignatureProvider.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Verify](M_Tessa_Platform_HashSignatureProvider_Verify.htm)|  Проверяет
валидность электронной цифровой подписи для заданных бинарных данных лицензии.  
(Унаследован от
[HashSignatureProvider](T_Tessa_Platform_HashSignatureProvider.htm))  
[VerifyCore](M_Tessa_Platform_HashSignatureProvider_VerifyCore.htm)|
Проверяет валидность электронной цифровой подписи для заданных бинарных данных
лицензии.  
(Унаследован от
[HashSignatureProvider](T_Tessa_Platform_HashSignatureProvider.htm))  
##  __Методы расширения
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
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
