# RuntimeHelper - поля
##  __Поля
[ConfigRootPathEnvironmentVariable](F_Chronos_Platform_RuntimeHelper_ConfigRootPathEnvironmentVariable.htm)|
Имя переменной окружения, в которой выполняется поиск конфигурационных файлов,
таких как app.json и extensions.xml. Если переменная равна точке ".", то
используется текущая папка приложения Directory.GetCurrentDirectory(). Если
переменная не задана, то выполняется поиск относительно папки Tessa.dll
вызовом
[GetActualLocationFolder(Assembly)](M_Chronos_Platform_PlatformExtensions_GetActualLocationFolder.htm).  
---|---  
## __См. также
#### Ссылки
[RuntimeHelper - ](T_Chronos_Platform_RuntimeHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
