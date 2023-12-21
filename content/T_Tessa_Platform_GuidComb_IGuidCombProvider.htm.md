# IGuidCombProvider - интерфейс
An interface for working with COMB GUIDs, implemented for both variants.
## __Definition
 **Пространство имён:**
[Tessa.Platform.GuidComb](N_Tessa_Platform_GuidComb.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IGuidCombProvider
VB __Копировать
     Public Interface IGuidCombProvider
C++ __Копировать
     public interface class IGuidCombProvider
F# __Копировать
     type IGuidCombProvider = interface end
##  __Методы
[Create()](M_Tessa_Platform_GuidComb_IGuidCombProvider_Create.htm)|  Returns a
new Guid COMB, consisting of a random Guid combined with the current UTC
timestamp.  
---|---  
[Create(DateTime)](M_Tessa_Platform_GuidComb_IGuidCombProvider_Create_1.htm)|
Returns a new Guid COMB, consisting of a random Guid combined with the
provided timestamp.  
[Create(Guid)](M_Tessa_Platform_GuidComb_IGuidCombProvider_Create_2.htm)|
Returns a new Guid COMB, consisting of the specified Guid combined with the
current UTC timestamp.  
[Create(Guid,
DateTime)](M_Tessa_Platform_GuidComb_IGuidCombProvider_Create_3.htm)|  Returns
a new Guid COMB, consisting of the provided Guid and provided timestamp.  
[GetTimestamp](M_Tessa_Platform_GuidComb_IGuidCombProvider_GetTimestamp.htm)|
Extracts the DateTime embedded in a COMB GUID of the current Variant.  
## __См. также
#### Ссылки
[Tessa.Platform.GuidComb - пространство имён](N_Tessa_Platform_GuidComb.htm)
