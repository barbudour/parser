# LicenseContainer - класс
Контейнер, содержащий лицензию и информацию о валидности её подписи.
Используется для сериализации и десериализации подписанной лицензии.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Licensing](N_Tessa_Platform_Licensing.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class LicenseContainer
VB __Копировать
     Public NotInheritable Class LicenseContainer
C++ __Копировать
     public ref class LicenseContainer sealed
F# __Копировать
     [<SealedAttribute>]
    type LicenseContainer = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ LicenseContainer
##  __Конструкторы
[LicenseContainer()](M_Tessa_Platform_Licensing_LicenseContainer__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию.  
---|---  
[LicenseContainer(License)](M_Tessa_Platform_Licensing_LicenseContainer__ctor_1.htm)|
Создаёт экземпляр класса с указанием лицензии, которая должна быть
сериализована.  
## __Свойства
[License](P_Tessa_Platform_Licensing_LicenseContainer_License.htm)|  Лицензия,
сериализация или десериализация которой производится.  
---|---  
[SignatureValid](P_Tessa_Platform_Licensing_LicenseContainer_SignatureValid.htm)|
Признак того, что подпись валидна после десериализации лицензии. Значение null
обозначает, что лицензия не была десериализована, поэтому информация о подписи
неизвестна.  
## __Методы
[Deserialize](M_Tessa_Platform_Licensing_LicenseContainer_Deserialize.htm)|
Десериализует подписанную лицензию. Информацию о валидности подписи можно
получить в свойстве
[SignatureValid](P_Tessa_Platform_Licensing_LicenseContainer_SignatureValid.htm).  
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
[Serialize](M_Tessa_Platform_Licensing_LicenseContainer_Serialize.htm)|
Сериализует подписанную лицензию.  
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
[Tessa.Platform.Licensing - пространство имён](N_Tessa_Platform_Licensing.htm)
