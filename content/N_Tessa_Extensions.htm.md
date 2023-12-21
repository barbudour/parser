# Tessa.Extensions - пространство имён
API для расширений.
##  __Классы
[AggregateExtensionStrategy](T_Tessa_Extensions_AggregateExtensionStrategy.htm)|
Стратегия, последователь агрегирующая выполнение других стратегий. Все методы
объекта являются потокобезопасными.  
---|---  
[AggregateFilterPolicy](T_Tessa_Extensions_AggregateFilterPolicy.htm)|
Политика, определяющих необходимость выполнения метода расширения посредством
последовательного исполнения заданного списка политик
[IFilterPolicy](T_Tessa_Extensions_IFilterPolicy.htm). Если хотя бы одна
указанная политика вернула false, то результатом метода будет false.  
[AssemblyRegistratorFinder](T_Tessa_Extensions_AssemblyRegistratorFinder.htm)|
Выполняет поиск типов объектов
[IRegistrator](T_Tessa_Extensions_IRegistrator.htm) в заданном каталоге
[IAssemblyCatalog](T_Tessa_Platform_Composition_IAssemblyCatalog.htm).  
[AsyncLazyResolvePolicy](T_Tessa_Extensions_AsyncLazyResolvePolicy.htm)|
Политика получения экземпляров расширений по заданной отложенной ссылке с
использованием асинхронности.  
[ContextFilterPolicy<TContext,
TPolicy>](T_Tessa_Extensions_ContextFilterPolicy_2.htm)|  Политика фильтрации
расширений, использующая политику
[IContextPolicy<TContext>](T_Tessa_Extensions_IContextPolicy_1.htm) для того,
чтобы не выполнять методы расширений, для которых выполняется условие для
контекста TContext. Если зарегистрировано несколько политик, то должны
выполняться все из них.  
[DefaultConstructorResolvePolicy](T_Tessa_Extensions_DefaultConstructorResolvePolicy.htm)|
Политика получения экземпляров расширений через вызов конструктора по
умолчанию для их типов.  
[DefaultConstructorSingletonResolvePolicy](T_Tessa_Extensions_DefaultConstructorSingletonResolvePolicy.htm)|
Политика получения экземпляров расширений через вызов конструктора по
умолчанию для их типов. Политика зарегистрирована по умолчанию для всех типов
расширений. Объект является синглтоном и доступен посредством свойства
[Instance](P_Tessa_Extensions_DefaultConstructorSingletonResolvePolicy_Instance.htm).
Для более оптимального создания экземпляров расширений используется объект
[DefaultConstructorResolvePolicy](T_Tessa_Extensions_DefaultConstructorResolvePolicy.htm),
который не является синглтоном и может содержать состояние.  
[DefaultDelegateContextPolicy](T_Tessa_Extensions_DefaultDelegateContextPolicy.htm)|
Политика, проверяющая условие для указанного контекста расширений, которое
задаётся как делегат Func<IExtensionContext, bool>. Выполняется для любых
типов расширений, даже если не была явно зарегистрирована.  
[DefaultExecuteStrategy](T_Tessa_Extensions_DefaultExecuteStrategy.htm)|
Стратегия, определяющая способ фильтрации расширений перед выполнением
посредством политики [IFilterPolicy](T_Tessa_Extensions_IFilterPolicy.htm).
Если указанная политика не зарегистрирована, то расширение выполняется обычным
образом. Все методы объекта являются потокобезопасными.  
[DefaultExtensionTraceListener](T_Tessa_Extensions_DefaultExtensionTraceListener.htm)|
Объект, выполняющий отслеживание событий, происходящих при выполнении
расширений. События записываются в
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)
как информационные сообщения.  
[DefaultFilterStrategy](T_Tessa_Extensions_DefaultFilterStrategy.htm)|
Стратегия, определяющая контекст фильтрации расширений перед выполнением
цепочки экземпляров расширений посредством политики
[IFilterPolicy](T_Tessa_Extensions_IFilterPolicy.htm). Если указанная политика
не зарегистрирована, то контекст фильтрации устанавливается равным null. Все
методы объекта являются потокобезопасными.  
[DefaultRegulateStrategy](T_Tessa_Extensions_DefaultRegulateStrategy.htm)|
Стратегия, упорядочивающая выполняемые расширения в соответствии с политикой
[IOrderPolicy](T_Tessa_Extensions_IOrderPolicy.htm). Все расширения,
зарегистрированные в контейнере с такой стратегией, обязаны содержать
указанную политику. Все методы объекта являются потокобезопасными.  
[DefaultResolveStrategy](T_Tessa_Extensions_DefaultResolveStrategy.htm)|
Стратегия, определяющая способ получения экземпляров расширений посредством
политики [IResolvePolicy](T_Tessa_Extensions_IResolvePolicy.htm). Все
расширения, зарегистрированные в контейнере с такой стратегией, обязаны
содержать указанную политику. Все методы объекта являются потокобезопасными.  
[DefaultTearDownStrategy](T_Tessa_Extensions_DefaultTearDownStrategy.htm)|
Стратегия, освобождающая ресурсы, занимаемые экземплярам расширений, для
которых зарегистрирована политика
[ITearDownPolicy](T_Tessa_Extensions_ITearDownPolicy.htm). Если указанная
политика не зарегистрирована, то никаких действий не выполняется. Все методы
объекта являются потокобезопасными.  
[DelegateContextPolicy<TContext>](T_Tessa_Extensions_DelegateContextPolicy_1.htm)|
Политика, проверяющая условие для указанного контекста расширений, которое
задаётся как делегат Func<TContext, bool>.  
[DisposeTearDownPolicy](T_Tessa_Extensions_DisposeTearDownPolicy.htm)|
Политика освобождения ресурсов, занятых экземплярами расширений, которые
реализуют интерфейс
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable).
Экземпляры расширений, не реализующие указанный интерфейс, игнорируются.  
[EmptyExtensionStrategy](T_Tessa_Extensions_EmptyExtensionStrategy.htm)|
Стратегия расширений, не выполняющая действий. Её регистрация может
использоваться для удаления зарегистрированной ранее стратегии на
соответствующем этапе. Все методы объекта являются потокобезопасными.  
[EmptyFilterPolicy](T_Tessa_Extensions_EmptyFilterPolicy.htm)|  Политика,
определяющая отсутствие фильтра для выполнения метода расширения. Может
использоваться для замещения существующей политики
[IFilterPolicy](T_Tessa_Extensions_IFilterPolicy.htm).  
[ExtensionAssembly](T_Tessa_Extensions_ExtensionAssembly.htm)|  Информация по
сборке с расширениями.  
[ExtensionAssemblyInfo](T_Tessa_Extensions_ExtensionAssemblyInfo.htm)|
Содержит информацию по зарегистрированным сборкам расширений.  
[ExtensionBuildKey](T_Tessa_Extensions_ExtensionBuildKey.htm)|  Ключ,
используемый для идентификации типа расширения.  
[ExtensionContainer](T_Tessa_Extensions_ExtensionContainer.htm)|  Контейнер
расширений. Все методы объекта являются потокобезопасными.  
[ExtensionContainerNames](T_Tessa_Extensions_ExtensionContainerNames.htm)|
Дополнительные имена контейнеров расширений, которые регистрируются в
контейнере Unity.  
[ExtensionExtensions](T_Tessa_Extensions_ExtensionExtensions.htm)|  Методы-
расширения для пространства имён Tessa.Extensions.  
[ExtensionPolicyContainer](T_Tessa_Extensions_ExtensionPolicyContainer.htm)|
Контейнер политик [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm),
ассоциированных с расширениями. Все методы объекта являются потокобезопасными.  
[ExtensionResolveKey](T_Tessa_Extensions_ExtensionResolveKey.htm)|  Ключ,
используемый для идентификации экземпляра расширения.  
[ExtensionsConfigHelper](T_Tessa_Extensions_ExtensionsConfigHelper.htm)|
Хэлперы для работы с конфигурационным файлом, описывающим сборки с плагинами.  
[ExtensionStrategyContext](T_Tessa_Extensions_ExtensionStrategyContext.htm)|
Контекст стратегии контейнера с расширениями
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm).  
[ExtensionTraceListener](T_Tessa_Extensions_ExtensionTraceListener.htm)|
Базовый класс для объекта, выполняющего отслеживание событий, происходящих при
выполнении расширений.  
[ExtensionTraceListenerHelper](T_Tessa_Extensions_ExtensionTraceListenerHelper.htm)|
Вспомогательные методы для трассировки расширений.  
[FuncResolvePolicy](T_Tessa_Extensions_FuncResolvePolicy.htm)|  Политика
получения экземпляров расширений посредством заданной функции.  
[InstanceResolvePolicy](T_Tessa_Extensions_InstanceResolvePolicy.htm)|
Политика получения экземпляров расширений по заданной ссылке.  
[LazyResolvePolicy](T_Tessa_Extensions_LazyResolvePolicy.htm)|  Политика
получения экземпляров расширений по заданной отложенной ссылке.  
[OrderPolicy](T_Tessa_Extensions_OrderPolicy.htm)|  Политика упорядочивания
расширений по этапам.  
[RegisterPoliciesStrategy](T_Tessa_Extensions_RegisterPoliciesStrategy.htm)|
Стратегия, выполняющая конфигурирование политик заданным способом для всех
расширений. Все методы объекта являются потокобезопасными.  
[RegistratorAttribute](T_Tessa_Extensions_RegistratorAttribute.htm)|  Атрибут,
указывающий метаданные объекта регистратора, на основании которых будет
выполняться регистрация расширений и зависимостей в Unity.  
[RegistratorBase](T_Tessa_Extensions_RegistratorBase.htm)|  Базовый класс для
объектов регистраторов, реализующих интерфейс
[IRegistrator](T_Tessa_Extensions_IRegistrator.htm).  
[RegistratorHelper](T_Tessa_Extensions_RegistratorHelper.htm)|
Вспомогательные средства для выполнения регистрации, используя найденные
объекты.  
[RegistratorImportingItem](T_Tessa_Extensions_RegistratorImportingItem.htm)|
Объект с информацией по импортированному типу регистратора расширений
[IRegistrator](T_Tessa_Extensions_IRegistrator.htm).  
[RegistratorMetadata](T_Tessa_Extensions_RegistratorMetadata.htm)|
Метаинформация по атрибуту
[RegistratorAttribute](T_Tessa_Extensions_RegistratorAttribute.htm),
представленная в сериализуемой форме.  
[SingletonResolvePolicy](T_Tessa_Extensions_SingletonResolvePolicy.htm)|
Политика получения экземпляров расширений, являющихся синглтонами, через вызов
конструктора по умолчанию для их типа.  
[UnityResolvePolicy](T_Tessa_Extensions_UnityResolvePolicy.htm)|  Политика
получения экземпляров расширений через заданный контейнер IUnityContainer.  
## __Структуры
[ExtensionExecutionKey](T_Tessa_Extensions_ExtensionExecutionKey.htm)|  Ключ,
используемый для идентификации выполняемого метода.  
---|---  
[ExtensionOrderKey](T_Tessa_Extensions_ExtensionOrderKey.htm)|  Ключ,
используемый для упорядочивания расширений по этапам.  
## __Интерфейсы
[IContextFilterPolicy<TContext>](T_Tessa_Extensions_IContextFilterPolicy_1.htm)|
Политика фильтрации расширений, использующая политику
[IContextPolicy<TContext>](T_Tessa_Extensions_IContextPolicy_1.htm) для того,
чтобы не выполнять методы расширений, для которых выполняется условие для
контекста TContext. Если зарегистрировано несколько политик, то должны
выполняться все из них.  
---|---  
[IContextPolicy<TContext>](T_Tessa_Extensions_IContextPolicy_1.htm)|
Политика, проверяющая условие для указанного контекста расширений.  
[IDefaultDelegateContextPolicy](T_Tessa_Extensions_IDefaultDelegateContextPolicy.htm)|
Политика, проверяющая условие для указанного контекста расширений, которое
задаётся как делегат Func<IExtensionContext, bool>. Выполняется для любых
типов расширений, даже если не была явно зарегистрирована.  
[IDelegateContextPolicy<TContext>](T_Tessa_Extensions_IDelegateContextPolicy_1.htm)|
Политика, проверяющая условие для указанного контекста расширений, которое
задаётся как делегат Func<TContext, bool>.  
[IExtension](T_Tessa_Extensions_IExtension.htm)|  Расширение. Может
дополнительно реализовывать интерфейс
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm) для
асинхронной инициализации после вызова конструктора.  
[IExtensionAssemblyInfo](T_Tessa_Extensions_IExtensionAssemblyInfo.htm)|
Содержит информацию по зарегистрированным сборкам расширений.  
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)|  Контейнер
расширений. Все методы объекта являются потокобезопасными.  
[IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)|  Контекст
асинхронного метода, выполняющего расширения. Содержит свойство
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)
для асинхронной отмены.  
[IExtensionExecutor<TExtension>](T_Tessa_Extensions_IExtensionExecutor_1.htm)|
Объект, выполняющий расширения заданного типа и определяющий время жизни
экземпляров расширений. Все методы объекта являются потокобезопасными.  
[IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm)|  Политика,
ассоциированная с расширениями.  
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm)|
Контейнер политик [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm),
ассоциированных с расширениями. Все методы объекта являются потокобезопасными.  
[IExtensionStrategy](T_Tessa_Extensions_IExtensionStrategy.htm)|  Стратегия
контейнера с расширениями
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm). Все методы
объекта являются потокобезопасными.  
[IExtensionStrategyContext](T_Tessa_Extensions_IExtensionStrategyContext.htm)|
Контекст стратегии контейнера с расширениями
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm).  
[IExtensionTraceListener](T_Tessa_Extensions_IExtensionTraceListener.htm)|
Объект, выполняющий отслеживание событий, происходящих при выполнении
расширений.  
[IExtensionTypeRegistrator<TExtension>](T_Tessa_Extensions_IExtensionTypeRegistrator_1.htm)|
Объект, выполняющий регистрацию типа расширения в контейнере
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm). Все методы
объекта являются потокобезопасными.  
[IFilterPolicy](T_Tessa_Extensions_IFilterPolicy.htm)|  Политика, определяющая
фильтр для выполнения метода расширения.  
[IOrderPolicy](T_Tessa_Extensions_IOrderPolicy.htm)|  Политика упорядочивания
расширений по этапам.  
[IRegistrator](T_Tessa_Extensions_IRegistrator.htm)|  Интерфейс, реализуемый в
объектах регистраторов. Помимо интерфейса также требуется указать атрибут
[RegistratorAttribute](T_Tessa_Extensions_RegistratorAttribute.htm).  
[IRegistratorMetadata](T_Tessa_Extensions_IRegistratorMetadata.htm)|
Метаинформация по атрибуту
[RegistratorAttribute](T_Tessa_Extensions_RegistratorAttribute.htm).  
[IResolvePolicy](T_Tessa_Extensions_IResolvePolicy.htm)|  Политика получения
экземпляров расширений.  
[ITearDownPolicy](T_Tessa_Extensions_ITearDownPolicy.htm)|  Политика
освобождения ресурсов, занятых экземплярами расширений.  
[ITraceableExtensionContext](T_Tessa_Extensions_ITraceableExtensionContext.htm)|
Контекст расширения, который отслеживается универсальными объектами
[IExtensionTraceListener](T_Tessa_Extensions_IExtensionTraceListener.htm),
доступными в платформе.  
## __Делегаты
[ExtensionMethodAsync<TContext>](T_Tessa_Extensions_ExtensionMethodAsync_1.htm)|
Метод, который можно асинхронно выполнить в расширении.  
---|---  
[ExtensionMethodReferenceAsync<TExtension,
TContext>](T_Tessa_Extensions_ExtensionMethodReferenceAsync_2.htm)|  Делегат,
возвращающий метод расширения, который можно асинхронно выполнить.  
[ExtensionPolicyConfigurator](T_Tessa_Extensions_ExtensionPolicyConfigurator.htm)|
Делегат, выполняющий конфигурирование политик в заданном контейнере.  
[ExtensionTypeConfigurator<TExtension>](T_Tessa_Extensions_ExtensionTypeConfigurator_1.htm)|
Делегат, выполняющий регистрацию типа расширения в контейнере.  
## __Перечисления
[ExceptionHandlingMode](T_Tessa_Extensions_ExceptionHandlingMode.htm)|  Режим
обработки исключений, возникающий в методах расширений. Может быть изменён в
т.ч. в методе
[NotifyException(IExtensionStrategyContext)](M_Tessa_Extensions_IExtensionTraceListener_NotifyException.htm).  
---|---  
[ExtensionStage](T_Tessa_Extensions_ExtensionStage.htm)|  Этап выполнения
расширения в цепочке расширений.  
[ExtensionStrategyStage](T_Tessa_Extensions_ExtensionStrategyStage.htm)|  Этап
выполнения стратегии для контейнера расширений
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm).  
[ExtensionTraceListenerType](T_Tessa_Extensions_ExtensionTraceListenerType.htm)|
Тип объекта
[DefaultExtensionTraceListener](T_Tessa_Extensions_DefaultExtensionTraceListener.htm),
выполняющего отслеживание событий, происходящих при выполнении расширений
карточек.  
[RegistratorTag](T_Tessa_Extensions_RegistratorTag.htm)|  Флаговое
перечисление с тегами регистратора, которые ограничивают область его
использования.
