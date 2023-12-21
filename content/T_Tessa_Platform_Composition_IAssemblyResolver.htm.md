# IAssemblyResolver - интерфейс
Объект, выполняющий получение объекта сборки, в ходе которого может
производиться её загрузка.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Composition](N_Tessa_Platform_Composition.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IAssemblyResolver
VB __Копировать
     Public Interface IAssemblyResolver
C++ __Копировать
     public interface class IAssemblyResolver
F# __Копировать
     type IAssemblyResolver = interface end
##  __Свойства
[FilePath](P_Tessa_Platform_Composition_IAssemblyResolver_FilePath.htm)|  Путь
к файлу со сборкой или null, если информация о местоположении сборки
неизвестна или сборка не располагается в файле на диске.  
---|---  
## __Методы
[TryResolve](M_Tessa_Platform_Composition_IAssemblyResolver_TryResolve.htm)|
Получает сборку, в процессе чего может выполняться загрузка сборки. Возвращает
null, то считается, что сборка была загружена, но она должна игнорироваться,
например, если она уже была загружена и проверена ранее.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform.Composition - пространство
имён](N_Tessa_Platform_Composition.htm)
