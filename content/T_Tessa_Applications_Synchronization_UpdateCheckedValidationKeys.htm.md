# UpdateCheckedValidationKeys - класс
Ключи валидации для проверки обновлений приложений.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class UpdateCheckedValidationKeys
VB __Копировать
     Public NotInheritable Class UpdateCheckedValidationKeys
C++ __Копировать
     public ref class UpdateCheckedValidationKeys abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type UpdateCheckedValidationKeys = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ UpdateCheckedValidationKeys
##  __Методы
[Register](M_Tessa_Applications_Synchronization_UpdateCheckedValidationKeys_Register.htm)|
Осуществляет регистрацию ключей валидации для объекта, осуществляющего
проверку наличия обновлений у приложений.  
---|---  
## __Поля
[AvailableApplicationsViewNotExist](F_Tessa_Applications_Synchronization_UpdateCheckedValidationKeys_AvailableApplicationsViewNotExist.htm)|
Представление не найдено.  
---|---  
[RemoteApplicationIsNotAvailable](F_Tessa_Applications_Synchronization_UpdateCheckedValidationKeys_RemoteApplicationIsNotAvailable.htm)|
Приложение на сервере отсутствует.  
[RemoteApplicationIsUpdated](F_Tessa_Applications_Synchronization_UpdateCheckedValidationKeys_RemoteApplicationIsUpdated.htm)|
Приложение на сервере имеет ту же разрядность и дату изменения, что и уже
скаченное приложение, обновление не требуется.  
[RemoteApplicationRequiresUpdate](F_Tessa_Applications_Synchronization_UpdateCheckedValidationKeys_RemoteApplicationRequiresUpdate.htm)|
Приложение на сервере имеет отличающуюся разрядность или дату изменения, что и
уже скаченное приложение, требуется обновление с сервера.  
[RemoteInfoIsDamaged](F_Tessa_Applications_Synchronization_UpdateCheckedValidationKeys_RemoteInfoIsDamaged.htm)|
Приложение на сервере повреждено.  
## __См. также
#### Ссылки
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
