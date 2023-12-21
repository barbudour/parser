# ApplicationCommands - класс
Типы команд, доступные в командной строке приложения по умолчанию.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ApplicationCommands
VB __Копировать
     Public NotInheritable Class ApplicationCommands
C++ __Копировать
     public ref class ApplicationCommands abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type ApplicationCommands = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ApplicationCommands
##  __Поля
[AutoStart](F_Tessa_Platform_Runtime_ApplicationCommands_AutoStart.htm)|
Команда, определяющая признак того, что приложение запущено с параметром "при
автозапуске системы". Если приложение поддерживает этот параметр, то экран
загрузки и окно приложения не отображается.  
---|---  
[BaseAddress](F_Tessa_Platform_Runtime_ApplicationCommands_BaseAddress.htm)|
Команда, устанавливающая базовый адрес веб-сервисов.  
[InstanceName](F_Tessa_Platform_Runtime_ApplicationCommands_InstanceName.htm)|
Команда, устанавливающая имя экземпляра, к которому выполняется подключение.  
[Link](F_Tessa_Platform_Runtime_ApplicationCommands_Link.htm)|  Команда,
устанавливающая режим обработки заданной ссылки сразу после запуска
приложения.  
[Login](F_Tessa_Platform_Runtime_ApplicationCommands_Login.htm)|  Команда,
устанавливающая логин пользователя.  
[MetadataCacheFilePath](F_Tessa_Platform_Runtime_ApplicationCommands_MetadataCacheFilePath.htm)|
Команда, определяющая путь к файлу с кэшом метаинформации, который должен
использоваться вместо стандартного файла.  
[Password](F_Tessa_Platform_Runtime_ApplicationCommands_Password.htm)|
Команда, устанавливающая пароль пользователя.  
[Publish](F_Tessa_Platform_Runtime_ApplicationCommands_Publish.htm)|  Команда,
определяющая режим публикации приложения вместо запуска.  
[PublishApplicationName](F_Tessa_Platform_Runtime_ApplicationCommands_PublishApplicationName.htm)|
Команда определяющая имя с которым публикуется приложение  
[PublishClient32Bit](F_Tessa_Platform_Runtime_ApplicationCommands_PublishClient32Bit.htm)|
Команда, указывающая, что публикуемое приложение использует 32-битную
архитектуру. Если ключ указан, то приложение можно запустить на 32-битных ОС.
Требуется использовать совместно с командой
[Publish](F_Tessa_Platform_Runtime_ApplicationCommands_Publish.htm).  
[PublishClient64Bit](F_Tessa_Platform_Runtime_ApplicationCommands_PublishClient64Bit.htm)|
Команда, указывающая, что публикуемое приложение использует 64-битную
архитектуру. Если ключ указан, то приложение нельзя запустить на 32-битных ОС.
Требуется использовать совместно с командой
[Publish](F_Tessa_Platform_Runtime_ApplicationCommands_Publish.htm).  
[PublishForAdmin](F_Tessa_Platform_Runtime_ApplicationCommands_PublishForAdmin.htm)|
Команда, определяющая режим публикации приложения только для администраторов.
Требуется использовать совместно с командой
[Publish](F_Tessa_Platform_Runtime_ApplicationCommands_Publish.htm).  
[PublishGroupName](F_Tessa_Platform_Runtime_ApplicationCommands_PublishGroupName.htm)|
Команда определяющая группу публикации приложения  
[PublishQuiet](F_Tessa_Platform_Runtime_ApplicationCommands_PublishQuiet.htm)|
Команда, определяющая режим публикации приложения без использования UI, т.е. с
выводом только в лог. Требуется использовать совместно с командой
[Publish](F_Tessa_Platform_Runtime_ApplicationCommands_Publish.htm).  
[SkipWinAuth](F_Tessa_Platform_Runtime_ApplicationCommands_SkipWinAuth.htm)|
Команда, определяющая признак того, что при незаданных параметрах
логина/пароля пропускается попытка Windows-аутентификации.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
