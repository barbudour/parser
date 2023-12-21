# FileConverterExtensions - класс
Методы-расширения для пространства имён Tessa.FileConverters.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class FileConverterExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class FileConverterExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class FileConverterExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type FileConverterExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileConverterExtensions
##  __Методы
[GetOutputStreamOrThrow](M_Tessa_FileConverters_FileConverterExtensions_GetOutputStreamOrThrow.htm)|
Возвращает поток на выходной файл или выбрасывает исключение, если файл не
найден или произошла другая ошибка при его открытии. Возвращённый поток
необходимо закрыть вызовом
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose).  
---|---  
[GetRequestOrThrowAsync](M_Tessa_FileConverters_FileConverterExtensions_GetRequestOrThrowAsync.htm)|
Возвращает запрос на выполнение операции по конвертации заданной версии файла
в карточке. Возвращаемое значение гарантированно не равно null. Если параметры
файла не найдены по идентификатору версии, то выбрасывается исключение.  
[Has](M_Tessa_FileConverters_FileConverterExtensions_Has.htm)| Возвращает
признак того, что заданный флаг установлен.  
[HasAny](M_Tessa_FileConverters_FileConverterExtensions_HasAny.htm)|
Возвращает признак того, что один из заданных флагов установлен.  
[HasNot](M_Tessa_FileConverters_FileConverterExtensions_HasNot.htm)|
Возвращает признак того, что заданный флаг не установлен.  
[RegisterFileConverterExtensionTypes](M_Tessa_FileConverters_FileConverterExtensions_RegisterFileConverterExtensionTypes.htm)|
Выполняет регистрацию стандартных типов расширений для конвертеров файлов.  
[RegisterFileConvertersOnServer](M_Tessa_FileConverters_FileConverterExtensions_RegisterFileConvertersOnServer.htm)|
Выполняет регистрацию API конвертации файлов. Регистрация требует серверных
зависимостей.  
[RegisterWorker<T>](M_Tessa_FileConverters_FileConverterExtensions_RegisterWorker__1.htm)|
Выполняет регистрацию реализации
[IFileConverterWorker](T_Tessa_FileConverters_IFileConverterWorker.htm) для
конвертации файла в формат outputFormat. Рекомендуется вызывать в методе
[FinalizeRegistration()](M_Tessa_Extensions_IRegistrator_FinalizeRegistration.htm).
Если не указать параметр overwrite равным true, то метод не выполнит действий,
когда тип уже зарегистрирован (но и исключений не выбросит). Также метод не
выполняет действий, когда в контейнере container не зарегистрирована
зависимость
[IFileConverterAggregateWorker](T_Tessa_FileConverters_IFileConverterAggregateWorker.htm)
(при инициализации на сервере по умолчанию регистрация есть).  
[ResolveWorker](M_Tessa_FileConverters_FileConverterExtensions_ResolveWorker.htm)|
Получает объект
[IFileConverterWorker](T_Tessa_FileConverters_IFileConverterWorker.htm) из
контейнера для конвертации файла в формат outputFormat. Если объект не
зарегистрирован, то выбрасывается исключение.  
[TryResolveWorker](M_Tessa_FileConverters_FileConverterExtensions_TryResolveWorker.htm)|
Получает объект
[IFileConverterWorker](T_Tessa_FileConverters_IFileConverterWorker.htm) из
контейнера для конвертации файла в формат outputFormat или null, если объект
не зарегистрирован.  
[WhenAnyFileConverterEventName](M_Tessa_FileConverters_FileConverterExtensions_WhenAnyFileConverterEventName.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым именам
событий конвертирования файлов. Используйте для замещения политики,
назначенной посредством метода
[WhenFileConverterEventNames(IExtensionPolicyContainer,
String[])](M_Tessa_FileConverters_FileConverterExtensions_WhenFileConverterEventNames.htm).
Для того, чтобы политика использовалась, требуется зарегистрировать политику
[FileConverterExtensionFilterPolicy](T_Tessa_FileConverters_FileConverterExtensionFilterPolicy.htm).  
[WhenAnyFileConverterOutputFormat](M_Tessa_FileConverters_FileConverterExtensions_WhenAnyFileConverterOutputFormat.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым
выходным форматам конвертирования файлов. Используйте для замещения политики,
назначенной посредством метода
[WhenFileConverterOutputFormats(IExtensionPolicyContainer,
FileConverterFormat[])](M_Tessa_FileConverters_FileConverterExtensions_WhenFileConverterOutputFormats.htm).
Для того, чтобы политика использовалась, требуется зарегистрировать политику
[FileConverterExtensionFilterPolicy](T_Tessa_FileConverters_FileConverterExtensionFilterPolicy.htm).  
[WhenFileConverterEventNames](M_Tessa_FileConverters_FileConverterExtensions_WhenFileConverterEventNames.htm)|
Регистрирует политику фильтрации выполнения методов расширений по имени
события конвертирования файлов, которое входит в заданный список имён. Для
того, чтобы политика использовалась, требуется зарегистрировать политику
[FileConverterExtensionFilterPolicy](T_Tessa_FileConverters_FileConverterExtensionFilterPolicy.htm).  
[WhenFileConverterFunc](M_Tessa_FileConverters_FileConverterExtensions_WhenFileConverterFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[IFileConverterExtension](T_Tessa_FileConverters_IFileConverterExtension.htm)
в соответствии с функцией isAllowedFunc, которая проверяет контекст
расширений. Если зарегистрировано несколько политик, то должны выполняться все
из них.  
[WhenFileConverterOutputFormats](M_Tessa_FileConverters_FileConverterExtensions_WhenFileConverterOutputFormats.htm)|
Регистрирует политику фильтрации выполнения методов расширений по выходному
формату конвертирования файлов, который входит в заданный список форматов. Для
того, чтобы политика использовалась, требуется зарегистрировать политику
[FileConverterExtensionFilterPolicy](T_Tessa_FileConverters_FileConverterExtensionFilterPolicy.htm).  
## __См. также
#### Ссылки
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
