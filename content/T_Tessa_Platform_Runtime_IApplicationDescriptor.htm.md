# IApplicationDescriptor - интерфейс
Объект, описывающий текущее приложение, которое определяется по клиентской
сессии [ISession](T_Tessa_Platform_Runtime_ISession.htm). Объект недоступен на
сервере.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationDescriptor
VB __Копировать
     Public Interface IApplicationDescriptor
C++ __Копировать
     public interface class IApplicationDescriptor
F# __Копировать
     type IApplicationDescriptor = interface end
##  __Свойства
[Alias](P_Tessa_Platform_Runtime_IApplicationDescriptor_Alias.htm)|  Алиас
приложения, который может использоваться для формирования пути к папкам
приложения или в ссылках, или null, если алиас неизвестен.  
---|---  
[ApplicationFolder](P_Tessa_Platform_Runtime_IApplicationDescriptor_ApplicationFolder.htm)|
Путь к папке, из которой запущено приложение.  
[ApplicationVersion](P_Tessa_Platform_Runtime_IApplicationDescriptor_ApplicationVersion.htm)|
Версия приложения.  
[CacheFolder](P_Tessa_Platform_Runtime_IApplicationDescriptor_CacheFolder.htm)|
Путь к папке, из которой запущено приложение.  
[EntryAssembly](P_Tessa_Platform_Runtime_IApplicationDescriptor_EntryAssembly.htm)|
Сборка, которая была определена как сборка, запустившая приложение. Значение
не равно null.  
[Icon](P_Tessa_Platform_Runtime_IApplicationDescriptor_Icon.htm)|  Иконка
приложения или null, если иконка недоступна. Обычно иконка всегда доступна,
т.к. при невозможности получить иконку из внешнего файла, она загружается из
ресурсов сборки или же используется иконка по умолчанию.  
[Name](P_Tessa_Platform_Runtime_IApplicationDescriptor_Name.htm)| Имя
приложения.  
[SettingsFolder](P_Tessa_Platform_Runtime_IApplicationDescriptor_SettingsFolder.htm)|
Путь к папке с настройками приложения.  
##  __События
[Initializing](E_Tessa_Platform_Runtime_IApplicationDescriptor_Initializing.htm)|
Событие, выполняющее инициализацию параметров приложения через свойства в
аргументах событий, в т.ч. на основании конфигурационных файлов и настроек,
полученных от Tessa Applications.  
---|---  
## __Методы расширения
[GetNameWithBitness](M_Tessa_Platform_Runtime_RuntimeExtensions_GetNameWithBitness.htm)|
Возвращает имя приложения с суффиксом, указывающим на его 64-битность (если
процесс 64-битный).  
(Определяется
[RuntimeExtensions](T_Tessa_Platform_Runtime_RuntimeExtensions.htm))  
---|---  
[InitializeByDefault](M_Tessa_UI_UIExtensions_InitializeByDefault.htm)|
Добавляет обработчик события для инициализации дескриптора приложения. Метод
можно безопасно вызывать несколько раз.  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
[RemoveDefaultInitialization](M_Tessa_UI_UIExtensions_RemoveDefaultInitialization.htm)|
Удаляет обработчик события, добавленный методом
[InitializeByDefault(IApplicationDescriptor)](M_Tessa_UI_UIExtensions_InitializeByDefault.htm).  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
