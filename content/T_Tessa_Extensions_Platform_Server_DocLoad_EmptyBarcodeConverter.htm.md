# EmptyBarcodeConverter - класс
Реализация интерфейса
[IBarcodeConverter](T_Tessa_Extensions_Platform_Server_DocLoad_IBarcodeConverter.htm),
возвращающая -1 на все запросы. Этот класс зарегистрирован в платформенных
расширениях, и в типовых расширениях он переопределяется с актуальной
реализацией.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.DocLoad](N_Tessa_Extensions_Platform_Server_DocLoad.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class EmptyBarcodeConverter : IBarcodeConverter
VB __Копировать
     Public NotInheritable Class EmptyBarcodeConverter
    	Implements IBarcodeConverter
C++ __Копировать
     public ref class EmptyBarcodeConverter sealed : IBarcodeConverter
F# __Копировать
     [<SealedAttribute>]
    type EmptyBarcodeConverter = 
        class
            interface IBarcodeConverter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ EmptyBarcodeConverter
Implements
    [IBarcodeConverter](T_Tessa_Extensions_Platform_Server_DocLoad_IBarcodeConverter.htm)
##  __Конструкторы
[EmptyBarcodeConverter](M_Tessa_Extensions_Platform_Server_DocLoad_EmptyBarcodeConverter__ctor.htm)|
Инициализирует новый экземпляр класса EmptyBarcodeConverter  
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
[GetBarcodeForRead](M_Tessa_Extensions_Platform_Server_DocLoad_EmptyBarcodeConverter_GetBarcodeForRead.htm)|
Получение ID штрих-кода в zxing см ZXing.BarcodeFormat  
[GetBarcodeForWrite](M_Tessa_Extensions_Platform_Server_DocLoad_EmptyBarcodeConverter_GetBarcodeForWrite.htm)|
Получение ID штрих-кода в Barcode.  
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
[Tessa.Extensions.Platform.Server.DocLoad - пространство
имён](N_Tessa_Extensions_Platform_Server_DocLoad.htm)
