# IRegistry<TItem> \- интерфейс
Описание интерфейса реестра объектов
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Workplaces.WebChart.Palette](N_Tessa_Extensions_Default_Client_Workplaces_WebChart_Palette.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IRegistry<out TItem>
    where TItem : class, ITypeIdentifier
VB __Копировать
     Public Interface IRegistry(Of Out TItem As {Class, ITypeIdentifier})
C++ __Копировать
    generic<typename TItem>
    where TItem : ref class, ITypeIdentifier
    public interface class IRegistry
F# __Копировать
     type IRegistry<'TItem when 'TItem : not struct and ITypeIdentifier> = interface end
#### Параметры типа
TItem
     Тип элемента реестра 
## __Свойства
[Items](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_Palette_IRegistry_1_Items.htm)|
Gets Список объектов реестра  
---|---  
## __Методы
[TryGetItem](M_Tessa_Extensions_Default_Client_Workplaces_WebChart_Palette_IRegistry_1_TryGetItem.htm)|
Осуществляет поиск объекта по его идентификатору. В случае если объект с
указанным идентификатором не найден в реестре возвращает null  
---|---  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Client.Workplaces.WebChart.Palette - пространство
имён](N_Tessa_Extensions_Default_Client_Workplaces_WebChart_Palette.htm)
