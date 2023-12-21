# PlatformExtensions - класс
Методы-расширения для пространства имён Tessa.Platform, а также методы-
расширения для классов общего назначения из других библиотек.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class PlatformExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class PlatformExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class PlatformExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type PlatformExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PlatformExtensions
##  __Методы
[AddBytes](M_Tessa_Platform_PlatformExtensions_AddBytes.htm)|  Вычисляет и
добавляет хэш-код для массива байт.  
---|---  
[AddDirectorySeparatorToPathEnd](M_Tessa_Platform_PlatformExtensions_AddDirectorySeparatorToPathEnd.htm)|
Добавляет в конец пути разделитель каталогов.  
[AppendElements<T>(StringBuilder, IEnumerable<T>, Action<StringBuilder, Int32,
T>)](M_Tessa_Platform_PlatformExtensions_AppendElements__1.htm)|  
[AppendElements<T>(StringBuilder, IEnumerable<T>, String,
Action<StringBuilder,
T>)](M_Tessa_Platform_PlatformExtensions_AppendElements__1_1.htm)|  
[AppendEscaped(StringBuilder, String, Char,
Char)](M_Tessa_Platform_PlatformExtensions_AppendEscaped.htm)|  
[AppendEscaped(StringBuilder, String, Char, Char, Char,
Char)](M_Tessa_Platform_PlatformExtensions_AppendEscaped_1.htm)|  
[AppendHexademical](M_Tessa_Platform_PlatformExtensions_AppendHexademical.htm)|  
[AppendIndent](M_Tessa_Platform_PlatformExtensions_AppendIndent.htm)|
Вставляет указанное число символов табуляции.  
[AppendSpaces](M_Tessa_Platform_PlatformExtensions_AppendSpaces.htm)|
Вставляет указанное число табуляций состоящей из пробелов.  
[ComputeHash(Byte[])](M_Tessa_Platform_PlatformExtensions_ComputeHash.htm)|
Возвращает массив байт с криптостойким хеш-значением для заданного массива
байт с данными.  
[ComputeHash(Byte[],
Byte[])](M_Tessa_Platform_PlatformExtensions_ComputeHash_1.htm)|  Возвращает
массив байт с криптостойким хеш-значением для заданного массива байт с данными
и заданного ключа, используемого для хеширования.  
[CreateGlobalCache<T>](M_Tessa_Platform_PlatformExtensions_CreateGlobalCache__1.htm)|
Создаёт глобальный кэш при помощи конструктора, который принимает уникальное
имя кэша в параметре instanceName и опционально объект
[IUnityDisposableContainer](T_Tessa_Platform_IUnityDisposableContainer.htm).  
[DisposeAllRegistrationsAsync](M_Tessa_Platform_PlatformExtensions_DisposeAllRegistrationsAsync.htm)|
Освобождает ресурсы для всех экземпляров, которые были зарегистрированы в
[IUnityDisposableContainer](T_Tessa_Platform_IUnityDisposableContainer.htm),
который в свою очередь зарегистрирован в текущем контейнере. Метод не
выбрасывает исключений, кроме
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception).  
[EndsWithDirectorySeparator](M_Tessa_Platform_PlatformExtensions_EndsWithDirectorySeparator.htm)|
Проверяет наличие разделителя пути в конце строки path.  
[FinalizeClientRegistration](M_Tessa_Platform_PlatformExtensions_FinalizeClientRegistration.htm)|
Завершает регистрацию клиента приложений.  
[FinalizeServerRegistration](M_Tessa_Platform_PlatformExtensions_FinalizeServerRegistration.htm)|
Завершает регистрацию сервера приложений.  
[FromCurrentSynchronizationContextSafe](M_Tessa_Platform_PlatformExtensions_FromCurrentSynchronizationContextSafe.htm)|
Возвращает диспетчер асинхронных задач из текущего контекста синхронизации.
Метод аналогичен вызову TaskScheduler.FromCurrentSynchronizationContext() за
тем исключением, что при отсутствии текущего контекста синхронизации будет
возвращён диспетчер currentScheduler. Контекст может отсутствовать в
консольных приложениях и в Unit-тестах. Пример использования:
TaskScheduler.Current.FromCurrentSynchronizationContextSafe().  
[FromXmlStringCore](M_Tessa_Platform_PlatformExtensions_FromXmlStringCore.htm)|
Реализация метода RSACryptoServiceProvider.FromXmlString(...), которая
функционирует для рантайма .NET Core. Реализация по умолчанию работает для
.NET Framework, но не работает для .NET Core. Эта реализация работает для
любого рантайма, поэтому рекомендуется использовать её.  
[GetActualLocationFileName](M_Tessa_Platform_PlatformExtensions_GetActualLocationFileName.htm)|
Возвращает действительное местоположение сборки (обычно это местоположение до
того, как сборка была скопирована механизмом shadow copy). При этом
используется делегат
[AssemblyResolveActualLocationFunc](P_Tessa_Platform_Runtime_RuntimeHelper_AssemblyResolveActualLocationFunc.htm)
или метод
[GetLocationFileNameFromCodeBase(Assembly)](M_Tessa_Platform_PlatformExtensions_GetLocationFileNameFromCodeBase.htm),
если делегат не был определён.  
[GetActualLocationFolder](M_Tessa_Platform_PlatformExtensions_GetActualLocationFolder.htm)|
Возвращает действительное местоположение сборки (обычно это местоположение до
того, как сборка была скопирована механизмом shadow copy). При этом
используется делегат
[AssemblyResolveActualLocationFunc](P_Tessa_Platform_Runtime_RuntimeHelper_AssemblyResolveActualLocationFunc.htm)
или метод
[GetLocationFolderFromCodeBase(Assembly)](M_Tessa_Platform_PlatformExtensions_GetLocationFolderFromCodeBase.htm),
если делегат не был определён.  
[GetAwaiter](M_Tessa_Platform_PlatformExtensions_GetAwaiter.htm)|
Предоставляет функциональность await для
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle).
Задача возвращает true, если ожидание handle было завершено, или false, если
ожидание завершилось таймаутом.  
[GetBytesWithPreamble](M_Tessa_Platform_PlatformExtensions_GetBytesWithPreamble.htm)|
Возвращает массив байт, кодирующий заданную строку вместе с BOM.  
[GetCardinality](M_Tessa_Platform_PlatformExtensions_GetCardinality.htm)|
Возвращает мощность битового массива, т.е. число установленных в единицу бит.  
[GetConstantHashCode(Byte[])](M_Tessa_Platform_PlatformExtensions_GetConstantHashCode.htm)|
Возвращает постоянный хеш-код для массива байт, значение которого не зависит
от текущего процесса.  
[GetConstantHashCode(ReadOnlySpan<Byte>)](M_Tessa_Platform_PlatformExtensions_GetConstantHashCode_1.htm)|
Возвращает постоянный хеш-код для списка байт в виде
[ReadOnlySpan<T>](https://learn.microsoft.com/dotnet/api/system.readonlyspan-1),
значение которого не зависит от текущего процесса.  
[GetConstantHashCode(Span<Byte>)](M_Tessa_Platform_PlatformExtensions_GetConstantHashCode_2.htm)|
Возвращает постоянный хеш-код для списка байт в виде
[Span<T>](https://learn.microsoft.com/dotnet/api/system.span-1), значение
которого не зависит от текущего процесса.  
[GetConstantHashCode(String)](M_Tessa_Platform_PlatformExtensions_GetConstantHashCode_3.htm)|
Возвращает постоянный хеш-код для строки, значение которого не зависит от
текущего процесса.  
[GetDescription](M_Tessa_Platform_PlatformExtensions_GetDescription.htm)|
Возвращает описание, указанное в строке атрибута [Description] для заданного
значения перечисления.  
[GetDisplayValue](M_Tessa_Platform_PlatformExtensions_GetDisplayValue.htm)|
Возвращает отображаемое значение для типа сообщения о валидации.  
[GetEnumerableElementTypes](M_Tessa_Platform_PlatformExtensions_GetEnumerableElementTypes.htm)|
Возвращает типы элементов для всех реализаций интерфейса перечисления
IEnumerable<T>, который реализует заданный тип type, или null, если тип не
реализует интерфейс перечисления. Например, тип string реализует
IEnumerable<char>, поэтому вызов метода вернёт единственный тип typeof(char).  
[GetFullText](M_Tessa_Platform_PlatformExtensions_GetFullText.htm)|
Возвращает полную информацию по заданному исключению, включая серверный
стектрейс для
[FaultException](https://learn.microsoft.com/dotnet/api/system.servicemodel.faultexception)
и текст нескольких исключений для
[AggregateException](https://learn.microsoft.com/dotnet/api/system.aggregateexception).
Для обычных исключений результат аналогичен вызову метода
[ToString()](https://learn.microsoft.com/dotnet/api/system.exception.tostring#system-
exception-tostring).  
[GetHashedString](M_Tessa_Platform_PlatformExtensions_GetHashedString.htm)|
Возвращает строку, содержащую криптостойкое хеш-значение от текущей строки.  
[GetInterfaceElementTypes](M_Tessa_Platform_PlatformExtensions_GetInterfaceElementTypes.htm)|
Возвращает список типов элементов во всех реализуемых интерфейсах
genericInterfaceType. Возвращаемое значение не равно null. Например, если в
genericInterfaceType указан тип typeof(IEnumerable<T>), и класс реализует
интерфейсы IEnumerable<string> и IEnumerable<object>, то будет возвращён
массив из двух типов: typeof(string) и typeof(object).  
[GetLocationFileNameFromCodeBase](M_Tessa_Platform_PlatformExtensions_GetLocationFileNameFromCodeBase.htm)|
Возвращает полный путь к файлу сборки.  
[GetLocationFolderFromCodeBase](M_Tessa_Platform_PlatformExtensions_GetLocationFolderFromCodeBase.htm)|
Возвращает путь к папке со сборкой. Используйте метод
[GetActualLocationFolder(Assembly)](M_Tessa_Platform_PlatformExtensions_GetActualLocationFolder.htm),
если может потребоваться глобально переопределить местоположение сборки.  
[GetNotNullableType](M_Tessa_Platform_PlatformExtensions_GetNotNullableType.htm)|
Возвращает вложенный тип для
[Nullable<T>](https://learn.microsoft.com/dotnet/api/system.nullable-1), если
type является подтипом от
[Nullable<T>](https://learn.microsoft.com/dotnet/api/system.nullable-1), в
противном случае возвращает исходный type. Например, если передать
typeof(Nullable<DateTime>), то метод вернёт typeof(DateTime), а если передать
typeof(DateTime), то метод вернёт его же.  
[GetResourceStream](M_Tessa_Platform_PlatformExtensions_GetResourceStream.htm)|
Возвращает [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)
для указанного файла в ресурсах манифеста.  
[GetService<T>](M_Tessa_Platform_PlatformExtensions_GetService__1.htm)|  
[GetShortText](M_Tessa_Platform_PlatformExtensions_GetShortText.htm)|
Возвращает краткую информацию по заданному исключению, что обычно
соответствует
[Message](https://learn.microsoft.com/dotnet/api/system.exception.message#system-
exception-message).  
[GetShortTypeName](M_Tessa_Platform_PlatformExtensions_GetShortTypeName.htm)|
Gives a shortened assemblyQualifiedName of the type, with only its fullName
and the name of its assembly. Does the same for its generic type parameters if
it has any.  
[GetStatusCode](M_Tessa_Platform_PlatformExtensions_GetStatusCode.htm)|
Возвращает код ошибки HTTP-запроса в зависимости от вида исключения. Для
неизвестных исключений возвращается
[InternalServerError](https://learn.microsoft.com/dotnet/api/system.net.httpstatuscode).  
[GetStringFromEmbeddedResource(Assembly,
String)](M_Tessa_Platform_PlatformExtensions_GetStringFromEmbeddedResource.htm)|
Возвращает строку с содержимым файла, встроенным в сборку как Embedded
Resource.  
[GetStringFromEmbeddedResource(Type,
String)](M_Tessa_Platform_PlatformExtensions_GetStringFromEmbeddedResource_1.htm)|
Возвращает строку с содержимым файла, встроенным в сборку как Embedded
Resource.  
[Has(ConfigurationFlags,
ConfigurationFlags)](M_Tessa_Platform_PlatformExtensions_Has.htm)| Возвращает
признак того, что заданный флаг установлен.  
[Has(TessaPlatformFeature,
TessaPlatformFeature)](M_Tessa_Platform_PlatformExtensions_Has_1.htm)|
Возвращает признак того, что заданный флаг установлен.  
[Has(TessaServerConfigFlags,
TessaServerConfigFlags)](M_Tessa_Platform_PlatformExtensions_Has_2.htm)|
Возвращает признак того, что заданный флаг установлен.  
[HasAny(ConfigurationFlags,
ConfigurationFlags)](M_Tessa_Platform_PlatformExtensions_HasAny.htm)|
Возвращает признак того, что один из заданных флагов установлен.  
[HasAny(TessaPlatformFeature,
TessaPlatformFeature)](M_Tessa_Platform_PlatformExtensions_HasAny_1.htm)|
Возвращает признак того, что один из заданных флагов установлен.  
[HasAny(TessaServerConfigFlags,
TessaServerConfigFlags)](M_Tessa_Platform_PlatformExtensions_HasAny_2.htm)|
Возвращает признак того, что один из заданных флагов установлен.  
[HasNot(ConfigurationFlags,
ConfigurationFlags)](M_Tessa_Platform_PlatformExtensions_HasNot.htm)|
Возвращает признак того, что заданный флаг не установлен.  
[HasNot(TessaPlatformFeature,
TessaPlatformFeature)](M_Tessa_Platform_PlatformExtensions_HasNot_1.htm)|
Возвращает признак того, что заданный флаг не установлен.  
[HasNot(TessaServerConfigFlags,
TessaServerConfigFlags)](M_Tessa_Platform_PlatformExtensions_HasNot_2.htm)|
Возвращает признак того, что заданный флаг не установлен.  
[Implements<T>](M_Tessa_Platform_PlatformExtensions_Implements__1.htm)|
Возвращает признак того, что тип реализует заданный интерфейс.  
[InternOrNull](M_Tessa_Platform_PlatformExtensions_InternOrNull.htm)|
Возвращает строку, которая была интернирована, или null, если исходная строка
была равна null.  
[InvokeNullableAsync<T>](M_Tessa_Platform_PlatformExtensions_InvokeNullableAsync__1.htm)|
Выполняет асинхронное ожидание для завершения события, принимающего аргументы
[DeferredEventArgs](T_Tessa_Platform_DeferredEventArgs.htm) или его наследник.  
[Limit](M_Tessa_Platform_PlatformExtensions_Limit.htm)|  Ограничивает длину
строки до максимальной maxLength, вставляя троеточие на конце, если длина
строки больше максимальной. Длина возвращаемого значения гарантированно не
больше maxLength вместе с троеточием, если maxLength не меньше 4, в противном
случае длина строки ограничивается до 4 символов.  
[LogException(ILogger, Exception,
LogLevel)](M_Tessa_Platform_PlatformExtensions_LogException.htm)|  Записывает
сообщение об исключении в лог с указанием необходимых деталей.  
[LogException(ILogger, String, Exception,
LogLevel)](M_Tessa_Platform_PlatformExtensions_LogException_1.htm)|
Записывает сообщение об исключении в лог с указанием необходимых деталей.  
[LogResult(ILogger, IValidationResultBuilder,
String)](M_Tessa_Platform_PlatformExtensions_LogResult.htm)|  Выполняет
логирование результата валидации и возвращает true, если результат содержал
хотя бы одно сообщение, которое было отправлено в лог.  
[LogResult(ILogger, IValidationResultBuilder,
ValidationLevel)](M_Tessa_Platform_PlatformExtensions_LogResult_1.htm)|
Выполняет логирование результата валидации и возвращает true, если результат
содержал хотя бы одно сообщение, которое было отправлено в лог.  
[LogResult(ILogger, ValidationResult,
String)](M_Tessa_Platform_PlatformExtensions_LogResult_2.htm)|  Выполняет
логирование результата валидации и возвращает true, если результат содержал
хотя бы одно сообщение, которое было отправлено в лог.  
[LogResult(ILogger, ValidationResult,
ValidationLevel)](M_Tessa_Platform_PlatformExtensions_LogResult_3.htm)|
Выполняет логирование результата валидации и возвращает true, если результат
содержал хотя бы одно сообщение, которое было отправлено в лог.  
[LogResult(ILogger, ValidationResult, ValidationLevel,
String)](M_Tessa_Platform_PlatformExtensions_LogResult_4.htm)|  Выполняет
логирование результата валидации и возвращает true, если результат содержал
хотя бы одно сообщение, которое было отправлено в лог.  
[LogResultItems(ILogger, IValidationResultBuilder,
String)](M_Tessa_Platform_PlatformExtensions_LogResultItems.htm)|  Выполняет
логирование результата валидации так, что каждое сообщение логируется отдельно
со своим уровнем логирования (Info, Warn, Error), и возвращает true, если
результат содержал хотя бы одно сообщение, которое было отправлено в лог.  
[LogResultItems(ILogger, IValidationResultBuilder,
ValidationLevel)](M_Tessa_Platform_PlatformExtensions_LogResultItems_1.htm)|
Выполняет логирование результата валидации так, что каждое сообщение
логируется отдельно со своим уровнем логирования (Info, Warn, Error), и
возвращает true, если результат содержал хотя бы одно сообщение, которое было
отправлено в лог.  
[LogResultItems(ILogger, ValidationResult,
String)](M_Tessa_Platform_PlatformExtensions_LogResultItems_2.htm)|  Выполняет
логирование результата валидации так, что каждое сообщение логируется отдельно
со своим уровнем логирования (Info, Warn, Error), и возвращает true, если
результат содержал хотя бы одно сообщение, которое было отправлено в лог.  
[LogResultItems(ILogger, ValidationResult,
ValidationLevel)](M_Tessa_Platform_PlatformExtensions_LogResultItems_3.htm)|
Выполняет логирование результата валидации так, что каждое сообщение
логируется отдельно со своим уровнем логирования (Info, Warn, Error), и
возвращает true, если результат содержал хотя бы одно сообщение, которое было
отправлено в лог.  
[NormalizeLineEndingsOnCurrentPlatform](M_Tessa_Platform_PlatformExtensions_NormalizeLineEndingsOnCurrentPlatform.htm)|
Заменяет символы перевода строки \r\n таким образом, чтобы они были корректны
(читаемы) на текущей платформе (Windows, Linux). Символы переводов строк \n в
стиле Unix не заменяются на \r\n, поскольку их можно прочитать в Windows без
замены.  
[NormalizeLineEndingsUnixStyle(String)](M_Tessa_Platform_PlatformExtensions_NormalizeLineEndingsUnixStyle.htm)|
Заменяет символы перевода строки \r\n на символ \n, который соответствует
переводу строки на Linux. На Windows он также читается. Рекомендуется
использовать для объектов конфигурации.  
[NormalizeLineEndingsUnixStyle(StringBuilder)](M_Tessa_Platform_PlatformExtensions_NormalizeLineEndingsUnixStyle_1.htm)|
Заменяет символы перевода строки \r\n на символ \n, который соответствует
переводу строки на Linux. На Windows он также читается. Рекомендуется
использовать для объектов конфигурации.  
[NormalizeLineEndingsWindowsStyle](M_Tessa_Platform_PlatformExtensions_NormalizeLineEndingsWindowsStyle.htm)|
Заменяет символ перевода строки \n на символы \r\n (если символ \r
отсутствовал), что соответствует переводу строки на Windows. Такие переводы
строк могут не читаться в некоторых текстовых редакторах на Linux.  
[NormalizePathOnCurrentPlatform](M_Tessa_Platform_PlatformExtensions_NormalizePathOnCurrentPlatform.htm)|
Заменяет символы в пути на файловой системе: "/" на "\" или наоборот, в
зависимости от текущей платформы (Windows, Linux).  
[NormalizeSpaces](M_Tessa_Platform_PlatformExtensions_NormalizeSpaces.htm)|
Заменяет все рядом стоящие пробельные символы, такие как пробелы и табуляции,
на одиночные пробелы.  
[NullIfEmpty](M_Tessa_Platform_PlatformExtensions_NullIfEmpty.htm)|
Возвращает null, если строка равна null или является пустой строкой, иначе
возвращает исходную строку.  
[OrderByAggregateExceptionTypes<T>](M_Tessa_Platform_PlatformExtensions_OrderByAggregateExceptionTypes__1.htm)|
Выполняет сортировку по типам исключений, содержащихся внутри исключения
[AggregateException](https://learn.microsoft.com/dotnet/api/system.aggregateexception),
для отображения пользователю (в виде окна валидации или в логах). Обычно
вызывается на коллекции aggregateException.Flatten().InnerException.  
[OrderByLocalized<T>](M_Tessa_Platform_PlatformExtensions_OrderByLocalized__1.htm)|
Сортирует значения последовательности по возрастанию по локализованному ключу,
который определяется для каждого элемента.  
[OrderByLocalizedDescending<T>](M_Tessa_Platform_PlatformExtensions_OrderByLocalizedDescending__1.htm)|
Сортирует значения последовательности по убыванию по локализованному ключу,
который определяется для каждого элемента.  
[PadBoth](M_Tessa_Platform_PlatformExtensions_PadBoth.htm)|  Выравнивает
строку пробелами по центру в поле заданного размера.  
[RegisterApplicationClientSettingsFromConfig](M_Tessa_Platform_PlatformExtensions_RegisterApplicationClientSettingsFromConfig.htm)|
Выполняет регистрацию объекта с клиентской конфигурацией
[ITessaClientSettings](T_Tessa_Platform_ITessaClientSettings.htm), настройки
которого загружаются из файла конфигурации посредством
[ConfigurationManager](T_Tessa_Platform_ConfigurationManager.htm). Метод
рекомендуется вызывать для клиентских приложений, таких как desktop-приложения
и консольные приложения.  
[RegisterApplicationServerSettingsFromConfig](M_Tessa_Platform_PlatformExtensions_RegisterApplicationServerSettingsFromConfig.htm)|
Выполняет регистрацию объекта с серверной конфигурацией
[ITessaServerSettings](T_Tessa_Platform_ITessaServerSettings.htm), настройки
которого загружаются из файла конфигурации посредством
[ConfigurationManager](T_Tessa_Platform_ConfigurationManager.htm). Метод
рекомендуется вызывать для серверных приложений, таких как плагины Chronos и
веб-приложения.  
[RegisterClientConsoleExtensionTypes](M_Tessa_Platform_PlatformExtensions_RegisterClientConsoleExtensionTypes.htm)|
Выполняет регистрацию типов расширений для консольных клиентских приложений в
контейнере [IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm).  
[RegisterDatabase](M_Tessa_Platform_PlatformExtensions_RegisterDatabase.htm)|
Выполняет регистрацию зависимостей, связанных с базой данных и с контейнерами
расширений. После вызова метода рекомендуется найти и зарегистрировать все
расширения.  
[RegisterDatabaseForPlugin](M_Tessa_Platform_PlatformExtensions_RegisterDatabaseForPlugin.htm)|
Выполняет регистрацию зависимостей для базы данных и контейнеров расширений
для плагина Chronos с указанием используемой сессии.  
[RegisterGlobalCache<T>](M_Tessa_Platform_PlatformExtensions_RegisterGlobalCache__1.htm)|
Выполняет регистрацию объекта глобального кэша в контейнере IUnityContainer.
Если в контейнере не зарегистрированы интерфейсы
[IUnityDisposableContainer](T_Tessa_Platform_IUnityDisposableContainer.htm)
или [IGlobalCacheLock](T_Tessa_Platform_Caching_IGlobalCacheLock.htm), то
метод выполняет такую регистрацию.  
[RegisterInConstructor<TEventArgs>](M_Tessa_Platform_PlatformExtensions_RegisterInConstructor__1.htm)|
Выполняет регистрацию текущего глобального кэша cache в контейнере container.
Все ресурсы глобального кэша могут быть освобождены, если регистрация в
контейнере container завершена по причине того, что все объекты контейнера уже
были освобождены. Возвращает признак того, что ресурсы глобального кэша не
были освобождены.  
[RegisterInterprocessDependenciesOnServer](M_Tessa_Platform_PlatformExtensions_RegisterInterprocessDependenciesOnServer.htm)|
Выполняет регистрацию фабрики
[ISharedEventSubscriberFactory](T_Tessa_Platform_IPC_ISharedEventSubscriberFactory.htm)
для использования на сервере.  
[RegisterPlatformSharedDependencies](M_Tessa_Platform_PlatformExtensions_RegisterPlatformSharedDependencies.htm)|
Выполняет регистрацию некоторых платформенных зависимостей, используемых как
на клиенте, так и на сервере.  
[RegisterProcessNameResolver](M_Tessa_Platform_PlatformExtensions_RegisterProcessNameResolver.htm)|
Выполняет регистрацию объекта
[IProcessNameResolver](T_Tessa_Platform_IProcessNameResolver.htm) с
реализацией по умолчанию.  
[RegisterServer](M_Tessa_Platform_PlatformExtensions_RegisterServer.htm)|
Выполняет регистрацию сервера приложений с заданными параметрами. После вызова
метода рекомендуется найти и зарегистрировать все расширения, а затем
завершить регистрацию методом [FinalizeServerRegistration(IUnityContainer,
IReadOnlyCollection<String>)](M_Tessa_Platform_PlatformExtensions_FinalizeServerRegistration.htm),
и, при необходимости, инициализировать локализацию методом
[InitializeLocalizationServiceAsync(IUnityContainer,
ILocalizationService[])](M_Tessa_Localization_LocalizationExtensions_InitializeLocalizationServiceAsync.htm).  
[RegisterServerExtensionTypes](M_Tessa_Platform_PlatformExtensions_RegisterServerExtensionTypes.htm)|
Выполняет регистрацию серверных типов расширений в контейнере
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm).  
[RegisterServerForPluginAsync(IUnityContainer, Func<ISessionToken>,
Boolean)](M_Tessa_Platform_PlatformExtensions_RegisterServerForPluginAsync.htm)|
Выполняет полный цикл регистрации сервера приложений для плагина Chronos с
указанием функции, которая возвращает токен используемой сессии.  
[RegisterServerForPluginAsync(IUnityContainer, ISessionToken,
Boolean)](M_Tessa_Platform_PlatformExtensions_RegisterServerForPluginAsync_1.htm)|
Выполняет полный цикл регистрации сервера приложений для плагина Chronos с
указанием используемой сессии. Генерирует новый идентификатор
[ServerRequestID](P_Tessa_Platform_Runtime_RuntimeHelper_ServerRequestID.htm),
если он не был заполнен перед этим вызовом.  
[RegisterServerSettings(IUnityContainer)](M_Tessa_Platform_PlatformExtensions_RegisterServerSettings.htm)|
Выполняет регистрацию объекта с серверной конфигурацией
[ITessaServerSettings](T_Tessa_Platform_ITessaServerSettings.htm) со
значениями по умолчанию.  
[RegisterServerSettings(IUnityContainer, Func<IUnityContainer,
ITessaServerSettings>)](M_Tessa_Platform_PlatformExtensions_RegisterServerSettings_1.htm)|
Выполняет регистрацию объекта с серверной конфигурацией
[ITessaServerSettings](T_Tessa_Platform_ITessaServerSettings.htm), для
которого задан способ создания посредством функции getSettingsFunc.  
[RegisterSharedExtensionTypes](M_Tessa_Platform_PlatformExtensions_RegisterSharedExtensionTypes.htm)|
Выполняет регистрацию типов расширений, актуальных и на клиенте, и на сервере,
в контейнере
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm).  
[RegisterSingletonWithClass<TFrom,
TTo>](M_Tessa_Platform_PlatformExtensions_RegisterSingletonWithClass__2.htm)|
Выполняет регистрацию синглтона так, что при получении объекта типа TFrom или
наследуемого объекта типа TTo будет возвращена ссылка на один и тот же
экземпляр.  
[ReplaceLineEndings](M_Tessa_Platform_PlatformExtensions_ReplaceLineEndings.htm)|
Возвращает заданную строку s, в которой переводы строк были заменены на
пробелы. Не удаляет пробелы по краям строки.  
[ReplaceLineEndingsAndTrim](M_Tessa_Platform_PlatformExtensions_ReplaceLineEndingsAndTrim.htm)|
Возвращает заданную строку s, в которой переводы строк были заменены на
пробелы, а затем все лишние пробелы по краям строки были удалены (включая
табуляции и бывшие переводы строк).  
[ReplaceNonBreakableToSpaces](M_Tessa_Platform_PlatformExtensions_ReplaceNonBreakableToSpaces.htm)|
Заменяем неделимые пробелы в строке на обычные.  
[ReplaceSpacesToNonBreakable](M_Tessa_Platform_PlatformExtensions_ReplaceSpacesToNonBreakable.htm)|
Заменяем обычные пробелы в строке на неделимые.  
[RequireService<T>](M_Tessa_Platform_PlatformExtensions_RequireService__1.htm)|  
[Resolve](M_Tessa_Platform_PlatformExtensions_Resolve.htm)|  Возвращает имя
процесса, пригодное для отображения пользователю.  
[RunWithMaxDegreeOfParallelismAsync<T>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
[SetFlag<T>](M_Tessa_Platform_PlatformExtensions_SetFlag__1.htm)|
Устанавливает или сбрасывает указанный флаг у флагового перечисления.  
[SetupAssemblyResolverFromConfiguration](M_Tessa_Platform_PlatformExtensions_SetupAssemblyResolverFromConfiguration.htm)|
Настраивает резолв сборок по параметрам из настроек сервера
[ITessaServerSettings](T_Tessa_Platform_ITessaServerSettings.htm) или настроек
клиента [ITessaClientSettings](T_Tessa_Platform_ITessaClientSettings.htm).
Если в контейнере отсутствует зарегистрированный объект, то метод не выполняет
действий.  
[SetupCacheInvalidation](M_Tessa_Platform_PlatformExtensions_SetupCacheInvalidation.htm)|
Настраивает сброс связанных глобальных кэшей.  
[SetupCardMetadataCacheInvalidation](M_Tessa_Platform_PlatformExtensions_SetupCardMetadataCacheInvalidation.htm)|
Настраивает сброс глобальных кэшей, связанных с изменением метаинформации
карточек.  
[SetupSchemeCacheInvalidation](M_Tessa_Platform_PlatformExtensions_SetupSchemeCacheInvalidation.htm)|
Настраивает сброс глобальных кэшей, связанных с изменением схемы данных.  
[SplitTextByWordsIntoMultipleLines](M_Tessa_Platform_PlatformExtensions_SplitTextByWordsIntoMultipleLines.htm)|
Разбивает строку на многострочный текст, где длина каждой строки определяется
в соответствии с указанной предпочитаемой длиной, но в действительности, может
быть несколько длиннее или короче. Строка разбивается только по словам, где
слово разделяется символами пробела (категория символов whitespace в Unicode).  
[StartOfWeek](M_Tessa_Platform_PlatformExtensions_StartOfWeek.htm)|
Возвращает дату на начало недели относительно заданной даты. Если передать
текущую дату, то метод вернёт дату начала текущей недели.  
[ToDictionaryAsync<TSource, TKey,
TElement>](M_Tessa_Platform_PlatformExtensions_ToDictionaryAsync__3.htm)|
Создает словарь [Dictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)
из объекта
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)
в соответствии с заданными функциями синхронного селектора ключа и
асинхронного селектора значения.  
[ToDictionaryStorage](M_Tessa_Platform_PlatformExtensions_ToDictionaryStorage.htm)|
Преобразует заданную хеш-таблицу в форму Dictionary<string, object>, которая
может затем использоваться в качестве хранилища для объектов
[StorageObject](T_Tessa_Platform_Storage_StorageObject.htm). Если объект
dictionary уже является требуемым типом, то выполняется преобразование типа
без копирования.  
[ToGuid(Byte[])](M_Tessa_Platform_PlatformExtensions_ToGuid.htm)|  Создаёт
уникальный идентификатор версии 3 по стандарту RFC 4122 из текущего массива
байт.  
[ToGuid(Int16)](M_Tessa_Platform_PlatformExtensions_ToGuid_1.htm)|
Преобразовать [Int16](https://learn.microsoft.com/dotnet/api/system.int16) в
[Guid](https://learn.microsoft.com/dotnet/api/system.guid). В первые два байта
сохраняется value как Big Endian, а в остальные - нули и специальные байты,
чтобы сохранить валидность значения
[Guid](https://learn.microsoft.com/dotnet/api/system.guid).  
[ToGuid(Int32)](M_Tessa_Platform_PlatformExtensions_ToGuid_2.htm)|
Преобразовать [Int16](https://learn.microsoft.com/dotnet/api/system.int16) в
[Guid](https://learn.microsoft.com/dotnet/api/system.guid). В первые четыре
байта сохраняется value как Big Endian, а в остальные - нули и специальные
байты, чтобы сохранить валидность значения
[Guid](https://learn.microsoft.com/dotnet/api/system.guid).  
[ToGuid(String)](M_Tessa_Platform_PlatformExtensions_ToGuid_3.htm)|  Создаёт
уникальный идентификатор версии 3 по стандарту RFC 4122 из текущей строки.  
[ToJson](M_Tessa_Platform_PlatformExtensions_ToJson.htm)|  Выполняет
сериализацию исключения в JSON. Может использоваться для передачи исключений
между сервером и клиентом.  
[ToPlainValidationResult](M_Tessa_Platform_PlatformExtensions_ToPlainValidationResult.htm)|
Выполняет сериализацию исключения в виде объекта
[PlainValidationResult](T_Tessa_Platform_Validation_PlainValidationResult.htm).
Может использоваться для передачи исключений между сервером и клиентом.  
[ToStringAndClear](M_Tessa_Platform_PlatformExtensions_ToStringAndClear.htm)|  
[ToStringAsConstructorParameters](M_Tessa_Platform_PlatformExtensions_ToStringAsConstructorParameters.htm)|
Преобразует уникальный идентификатор в строку, записанную в форме списка
параметров, которые можно передать в конструктор
[Guid](https://learn.microsoft.com/dotnet/api/system.guid). Например:
0x9165b6bc, 0x688a, 0x46f5, 0xbd, 0xe8, 0xda, 0x95, 0x95, 0x88, 0xe4, 0x18  
[ToStringLower](M_Tessa_Platform_PlatformExtensions_ToStringLower.htm)|
Преобразует логическое значение к строковому представлению в нижнем регистре.  
[ToTask](M_Tessa_Platform_PlatformExtensions_ToTask.htm)|  Создаёт задачу,
которая отмечается как завершённая, когда для
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle)
сработает сигнал. Задача возвращает true, если ожидание handle было завершено,
или false, если ожидание завершилось таймаутом.  
[ToXmlStringCore](M_Tessa_Platform_PlatformExtensions_ToXmlStringCore.htm)|
Реализация метода RSACryptoServiceProvider.ToXmlString(...), которая
функционирует для рантайма .NET Core. Реализация по умолчанию работает для
.NET Framework, но не работает для .NET Core. Эта реализация работает для
любого рантайма, поэтому рекомендуется использовать её.  
[TransformForOrientation](M_Tessa_Platform_PlatformExtensions_TransformForOrientation.htm)|
Производит трансформацию изображения в соответствии с заданным в свойствах
значением ориентации, удаляя при этом соответствующее свойство.  
[TryGetConfigurationException](M_Tessa_Platform_PlatformExtensions_TryGetConfigurationException.htm)|
Возвращает исключение, описывающее все ошибки, которые произошли при
инициализации конфигурации, или null, если ошибок не было. Такое исключение
можно выбросить, чтобы передать больше информации о проблеме с конфигурацией.  
[TryGetNestedInnerException](M_Tessa_Platform_PlatformExtensions_TryGetNestedInnerException.htm)|
Возвращает вложенное исключение для ex на любое число уровней вложенности,
которое удовлетворяет условию predicateFunc, или null, если такое вложенное
исключение не найдено.  
[TryResolve(IUnityContainer, Type,
String)](M_Tessa_Platform_PlatformExtensions_TryResolve.htm)|  Выполняет
резолв зависимости типа type с именем name и возвращает её, если резолв
успешен, или возвращает null, если не удалось выполнить резолв по любой
причине (например, тип не зарегистрирован или не зарегистрирована одна из его
зависимостей).  
[TryResolve<T>(IUnityContainer,
String)](M_Tessa_Platform_PlatformExtensions_TryResolve__1.htm)|  Выполняет
резолв зависимости типа T с именем name и возвращает её, если резолв успешен,
или возвращает default(T) (null), если не удалось выполнить резолв по любой
причине (например, тип не зарегистрирован или не зарегистрирована одна из его
зависимостей).  
[TryToInt16](M_Tessa_Platform_PlatformExtensions_TryToInt16.htm)|
Преобразовать [Guid](https://learn.microsoft.com/dotnet/api/system.guid) в
[Int16](https://learn.microsoft.com/dotnet/api/system.int16). Значение берется
из первых двух байтов как Big Endian.  
[TryToInt32](M_Tessa_Platform_PlatformExtensions_TryToInt32.htm)|
Преобразовать [Guid](https://learn.microsoft.com/dotnet/api/system.guid) в
[Int32](https://learn.microsoft.com/dotnet/api/system.int32). Значение берется
из первых четырёх байтов как Big Endian.  
[WaitAndUnwrap(Task)](M_Tessa_Platform_PlatformExtensions_WaitAndUnwrap.htm)|
Ожидает завершение асинхронной задачи без таймаутов. При возникновении
[AggregateException](https://learn.microsoft.com/dotnet/api/system.aggregateexception)
исключение "разворачивается" в исходное исключение.  
[WaitAndUnwrap(Task,
Int32)](M_Tessa_Platform_PlatformExtensions_WaitAndUnwrap_1.htm)|  Ожидает
завершение асинхронной задачи с указанным таймаутом. При возникновении
[AggregateException](https://learn.microsoft.com/dotnet/api/system.aggregateexception)
исключение "разворачивается" в исходное исключение.  
[WaitAndUnwrap(Task,
TimeSpan)](M_Tessa_Platform_PlatformExtensions_WaitAndUnwrap_2.htm)|  Ожидает
завершение асинхронной задачи с указанным таймаутом. При возникновении
[AggregateException](https://learn.microsoft.com/dotnet/api/system.aggregateexception)
исключение "разворачивается" в исходное исключение. Возвращает признак того,
что ожидание завершилось без таймаута.  
[WaitOneAsync(WaitHandle,
CancellationToken)](M_Tessa_Platform_PlatformExtensions_WaitOneAsync_1.htm)|
Асинхронно ожидает заданный объект
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle).
Ожидание выполняется без таймаута.  
[WaitOneAsync(WaitHandle, Int32,
CancellationToken)](M_Tessa_Platform_PlatformExtensions_WaitOneAsync.htm)|
Асинхронно ожидает заданный объект
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle).
Возвращает признак того, что ожидание завершилось при переходе объекта
waitHandle в сигнальное состояние, а не при наступлении таймаута.  
[WaitOneAsync(WaitHandle, TimeSpan,
CancellationToken)](M_Tessa_Platform_PlatformExtensions_WaitOneAsync_2.htm)|
Асинхронно ожидает заданный объект
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle).
Возвращает признак того, что ожидание завершилось при переходе объекта
waitHandle в сигнальное состояние, а не при наступлении таймаута.  
[WithoutMilliseconds](M_Tessa_Platform_PlatformExtensions_WithoutMilliseconds.htm)|
Возвращает объект
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime), полученный
из исходного за вычетом миллисекунд.  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
