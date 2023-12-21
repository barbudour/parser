# CurrentUserDataProtectionService - класс
Сервис шифрования данных связанных с текущим пользователем
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CurrentUserDataProtectionService : IDataProtectionService
VB __Копировать
     Public NotInheritable Class CurrentUserDataProtectionService
    	Implements IDataProtectionService
C++ __Копировать
     public ref class CurrentUserDataProtectionService sealed : IDataProtectionService
F# __Копировать
     [<SealedAttribute>]
    type CurrentUserDataProtectionService = 
        class
            interface IDataProtectionService
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CurrentUserDataProtectionService
Implements
    [IDataProtectionService](T_Tessa_Applications_IDataProtectionService.htm)
##  __Конструкторы
[CurrentUserDataProtectionService](M_Tessa_Applications_CurrentUserDataProtectionService__ctor.htm)|
Инициализирует новый экземпляр класса CurrentUserDataProtectionService  
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
[Protect](M_Tessa_Applications_CurrentUserDataProtectionService_Protect.htm)|
Осуществляет шифрование данных data  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Unprotect](M_Tessa_Applications_CurrentUserDataProtectionService_Unprotect.htm)|
Осуществляет расшифрование данных data  
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
[Protect](M_Tessa_Applications_DataProtectionServiceExtender_Protect.htm)|
Осуществляет шифрование строки данных data  
(Определяется
[DataProtectionServiceExtender](T_Tessa_Applications_DataProtectionServiceExtender.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Unprotect](M_Tessa_Applications_DataProtectionServiceExtender_Unprotect.htm)|
Осуществляет шифрование строки данных data  
(Определяется
[DataProtectionServiceExtender](T_Tessa_Applications_DataProtectionServiceExtender.htm))  
##  __См. также
#### Ссылки
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
