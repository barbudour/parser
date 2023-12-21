# FileSystemSynchronizationSource.TryGetApplicationPackage - метод
Осуществляет попытку получения пакета приложения. В случае если пакет
приложения не может быть получен возвращает null. Ошибки построения пакета
приложения записываются в validationResultBuilder
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationPackage TryGetApplicationPackage(
    	ValidationResultBuilder validationResultBuilder
    )
VB __Копировать
     Public Function TryGetApplicationPackage ( 
    	validationResultBuilder As ValidationResultBuilder
    ) As ApplicationPackage
C++ __Копировать
     public:
    ApplicationPackage^ TryGetApplicationPackage(
    	ValidationResultBuilder^ validationResultBuilder
    )
F# __Копировать
     member TryGetApplicationPackage : 
            validationResultBuilder : ValidationResultBuilder -> ApplicationPackage 
#### Параметры
validationResultBuilder
[ValidationResultBuilder](T_Tessa_Platform_Validation_ValidationResultBuilder.htm)
     Построитель результатов валидации 
#### Возвращаемое значение
[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)  
Пакет приложения или null, если
## __См. также
#### Ссылки
[FileSystemSynchronizationSource -
](T_Tessa_Applications_Synchronization_FileSystemSynchronizationSource.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
