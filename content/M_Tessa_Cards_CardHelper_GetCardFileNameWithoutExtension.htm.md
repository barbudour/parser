# CardHelper.GetCardFileNameWithoutExtension - метод
Возвращает корректное имя файла карточки без расширения по дайджесту карточки.
Может использоваться для определения имени файла для экспортируемой карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetCardFileNameWithoutExtension(
    	string digest
    )
VB __Копировать
     Public Shared Function GetCardFileNameWithoutExtension ( 
    	digest As String
    ) As String
C++ __Копировать
     public:
    static String^ GetCardFileNameWithoutExtension(
    	String^ digest
    )
F# __Копировать
     static member GetCardFileNameWithoutExtension : 
            digest : string -> string 
#### Параметры
digest [String](https://learn.microsoft.com/dotnet/api/system.string)
     Digest карточки, который может быть равен null или пустой строке. Может быть строкой локализации. 
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Корректное имя файла карточки.
##  __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
