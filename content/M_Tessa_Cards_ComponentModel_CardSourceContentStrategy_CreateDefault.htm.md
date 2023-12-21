# CardSourceContentStrategy.CreateDefault - метод
Создаёт экземпляр класса
[CardSourceContentStrategy](T_Tessa_Cards_ComponentModel_CardSourceContentStrategy.htm)
с параметрами по умолчанию при создании без контейнера Unity.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardSourceContentStrategy CreateDefault(
    	ICardFileSourceSettings fileSourceSettings,
    	IDbScope dbScope
    )
VB __Копировать
     Public Shared Function CreateDefault ( 
    	fileSourceSettings As ICardFileSourceSettings,
    	dbScope As IDbScope
    ) As CardSourceContentStrategy
C++ __Копировать
     public:
    static CardSourceContentStrategy^ CreateDefault(
    	ICardFileSourceSettings^ fileSourceSettings, 
    	IDbScope^ dbScope
    )
F# __Копировать
     static member CreateDefault : 
            fileSourceSettings : ICardFileSourceSettings * 
            dbScope : IDbScope -> CardSourceContentStrategy 
#### Параметры
fileSourceSettings
[ICardFileSourceSettings](T_Tessa_Cards_ICardFileSourceSettings.htm)
    Настройки для местоположений файлов.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, обеспечивающий взаимодействие с базой данных.
#### Возвращаемое значение
[CardSourceContentStrategy](T_Tessa_Cards_ComponentModel_CardSourceContentStrategy.htm)  
Созданный объект.
##  __См. также
#### Ссылки
[CardSourceContentStrategy -
](T_Tessa_Cards_ComponentModel_CardSourceContentStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
