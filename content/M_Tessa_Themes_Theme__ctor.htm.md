# Theme - конструктор
Создаёт экземпляр класса с указанием родительской темы.
## __Definition
 **Пространство имён:** [Tessa.Themes](N_Tessa_Themes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Theme(
    	Theme parentTheme = null
    )
VB __Копировать
     Public Sub New ( 
    	Optional parentTheme As Theme = Nothing
    )
C++ __Копировать
     public:
    Theme(
    	Theme^ parentTheme = nullptr
    )
F# __Копировать
     new : 
            ?parentTheme : Theme 
    (* Defaults:
            let _parentTheme = defaultArg parentTheme null
    *)
    -> Theme
#### Параметры
parentTheme [Theme](T_Tessa_Themes_Theme.htm) (Optional)
     Родительская тема, используемая для указания начальных значений в случае, если в текущей теме значения не заданы. Если параметр равен null, то используется тема по умолчанию. 
## __См. также
#### Ссылки
[Theme - ](T_Tessa_Themes_Theme.htm)
[Tessa.Themes - пространство имён](N_Tessa_Themes.htm)
