# ValidationKeys - класс
Стандартные ключи валидации.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Validation](N_Tessa_Platform_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ValidationKeys
VB __Копировать
     Public NotInheritable Class ValidationKeys
C++ __Копировать
     public ref class ValidationKeys abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type ValidationKeys = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ValidationKeys
##  __Поля
[ConfigurationIsSealed](F_Tessa_Platform_Validation_ValidationKeys_ConfigurationIsSealed.htm)|
Сообщение о том, что конфигурация на сервере в неизменяемом режиме, и
невозможно выполнить импорт и модификацию скриптов.  
---|---  
[ConfigurationIsStrictSecurity](F_Tessa_Platform_Validation_ValidationKeys_ConfigurationIsStrictSecurity.htm)|
Сообщение о том, что конфигурация на сервере в режиме повышенной безопасности,
и некоторые административные функции недоступны.  
[ErrorGettingExternalContent](F_Tessa_Platform_Validation_ValidationKeys_ErrorGettingExternalContent.htm)|
Ошибка при попытке получить контент из внешнего источника. {0} - Путь до
контента.  
[Exception](F_Tessa_Platform_Validation_ValidationKeys_Exception.htm)|  Было
выброшено исключение. Его тип указан в FieldName.  
[ExcessFilesInSubdirectory](F_Tessa_Platform_Validation_ValidationKeys_ExcessFilesInSubdirectory.htm)|
В поддиректории карточки обнаружен лишний файл. {0} - Имя лишнего файла. {1} -
Имя поддиректории в которой обнаружен лишний файл.  
[ExportSubdirectoryAlreadyExists](F_Tessa_Platform_Validation_ValidationKeys_ExportSubdirectoryAlreadyExists.htm)|
В папке {0} для карточки {1} уже существует одноименная подпапка, которая не
относится к карточке. Необходимо удалить, переименовать или переместить данную
подпапку, или экспортировать карточку с другим именем. {0} - Путь до папки
куда экспортируется карточка. {1} - Имя файла экспортируемой карточки.  
[OperationIsUnavailable](F_Tessa_Platform_Validation_ValidationKeys_OperationIsUnavailable.htm)|
Сообщение о том, что операция недоступна в текущем контексте (обычно при
вызове из клиентского приложения). {0} - идентификатор типа операции.  
[ParentSectionNotExistsInCardType](F_Tessa_Platform_Validation_ValidationKeys_ParentSectionNotExistsInCardType.htm)|
В карточке ID "{0}", колонка "{1}" в секции "{2}", ссылается на родительскую
секцию "{3}", которая отсутствует в типе карточки "{4}". {0} - ID карточки.
{1} - Имя колонки, которая ссылается на родительскую. {2} - Имя секции,
содержащей колонку. {3} - Имя родительской секции. {4} - Имя типа карточки.  
[PasswordExpiresSoon](F_Tessa_Platform_Validation_ValidationKeys_PasswordExpiresSoon.htm)|
Сообщение о том, что пароль текущего пользователя скоро истечёт и его надо
заменить. {0} - дата и время истечения пароля. {1} - дата и время истечения
пароля в UTC.  
[PlatformVersionsDiffer](F_Tessa_Platform_Validation_ValidationKeys_PlatformVersionsDiffer.htm)|
Сообщение о том, что версия сборки сервера отличается от версии сборки
клиента. {0} - версия сервера. {1} - дата сборки сервера. {2} - версия
клиента. {3} - дата сборки клиента.  
[PropertyHasInvalidItemsOrNotExists](F_Tessa_Platform_Validation_ValidationKeys_PropertyHasInvalidItemsOrNotExists.htm)|
Заданное свойство содержит неверные элементы или оно отсутствует в хранилище.  
[PropertyIsEmpty](F_Tessa_Platform_Validation_ValidationKeys_PropertyIsEmpty.htm)|
У заданного свойства пустое значение.  
[PropertyIsEmptyOrNotExists](F_Tessa_Platform_Validation_ValidationKeys_PropertyIsEmptyOrNotExists.htm)|
У заданного свойства пустое значение или свойство отсутствует в хранилище.  
[PropertyIsInvalid](F_Tessa_Platform_Validation_ValidationKeys_PropertyIsInvalid.htm)|
У заданного свойства некорректное значение.  
[PropertyIsInvalidOrNotExists](F_Tessa_Platform_Validation_ValidationKeys_PropertyIsInvalidOrNotExists.htm)|
У заданного свойства некорректное значение или свойство отсутствует в
хранилище.  
[PropertyNotExists](F_Tessa_Platform_Validation_ValidationKeys_PropertyNotExists.htm)|
Заданное свойство отсутствует в хранилище.  
[SmartMergeDuplicateIgnored](F_Tessa_Platform_Validation_ValidationKeys_SmartMergeDuplicateIgnored.htm)|
При слиянии игнорирован дубликат строки. {0} - Информация по дубликату  
[SmartMergeOptionsIncludedColumnsWithOtherTypes](F_Tessa_Platform_Validation_ValidationKeys_SmartMergeOptionsIncludedColumnsWithOtherTypes.htm)|
В опциях слияния наряду с IncludedColumns содержатся ExcludedColumns и/или
IgnoredColumns (IncludedColumns проигнорируются). {0} - Информация по
несоответсвию  
[TraceClientExtensionExecuted](F_Tessa_Platform_Validation_ValidationKeys_TraceClientExtensionExecuted.htm)|
Логируется информация по выполненному клиентскому расширению карточек.  
[TraceClientExtensionExecutedWithTime](F_Tessa_Platform_Validation_ValidationKeys_TraceClientExtensionExecutedWithTime.htm)|
Логируется информация по выполненному клиентскому расширению карточек с
указанием времени выполнения.  
[TraceServerExtensionExecuted](F_Tessa_Platform_Validation_ValidationKeys_TraceServerExtensionExecuted.htm)|
Логируется информация по выполненному серверному расширению карточек.  
[TraceServerExtensionExecutedWithTime](F_Tessa_Platform_Validation_ValidationKeys_TraceServerExtensionExecutedWithTime.htm)|
Логируется информация по выполненному серверному расширению карточек с
указанием времени выполнения.  
[WebClientIsForbidden](F_Tessa_Platform_Validation_ValidationKeys_WebClientIsForbidden.htm)|
Сообщение о том, что у сотрудника отсутствует доступ к web-клиенту. {0} -
краткое имя сотрудника, которому запрещён вход. {1} - идентификатор
сотрудника, которому запрещён вход.  
## __См. также
#### Ссылки
[Tessa.Platform.Validation - пространство
имён](N_Tessa_Platform_Validation.htm)
