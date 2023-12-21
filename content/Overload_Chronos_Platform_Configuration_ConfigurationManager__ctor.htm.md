# ConfigurationManager - конструктор
##  __Список перегрузок
[ConfigurationManager(ConfigurationObject, IEnumerable<KeyValuePair<String,
String>>)](M_Chronos_Platform_Configuration_ConfigurationManager__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств. После создания
объекта необходимо вызвать метод асинхронной инициализации
[InitializeAsync(CancellationToken)](M_Chronos_Platform_IAsyncInitializable_InitializeAsync.htm).  
---|---  
[ConfigurationManager(String, IEnumerable<KeyValuePair<String,
String>>)](M_Chronos_Platform_Configuration_ConfigurationManager__ctor_2.htm)|
Создаёт экземпляр класса с указанием полного пути до файла с конфигурацией.
Вызов конструктора не может завершиться исключением. После создания объекта
необходимо вызвать метод асинхронной инициализации
[InitializeAsync(CancellationToken)](M_Chronos_Platform_IAsyncInitializable_InitializeAsync.htm).  
[ConfigurationManager(Assembly, String, IEnumerable<KeyValuePair<String,
String>>)](M_Chronos_Platform_Configuration_ConfigurationManager__ctor_1.htm)|
Создаёт экземпляр класса с указанием сборки, рядом с которой лежит файл
конфигурации app.json. Вызов конструктора не может завершиться исключением.
После создания объекта необходимо вызвать метод асинхронной инициализации
[InitializeAsync(CancellationToken)](M_Chronos_Platform_IAsyncInitializable_InitializeAsync.htm).  
## __См. также
#### Ссылки
[ConfigurationManager -
](T_Chronos_Platform_Configuration_ConfigurationManager.htm)
[Chronos.Platform.Configuration - пространство
имён](N_Chronos_Platform_Configuration.htm)
